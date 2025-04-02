import pandas as pd
import json
import os
from datetime import datetime, timezone
from collections import defaultdict
from .obtain_ema_code import *
from .fetch_station_data import *
import logging
from typing import Dict, List, Optional, Tuple

# Configuración global
DEFAULT_START_DATE = '2025-01-01T00:00:00UTC'
REQUEST_DELAY = 3.0  # segundos entre solicitudes 
STATION_TIMEOUT = 30  # segundos máximo por estación
MAX_RETRIES = 3  # reintentos por estación

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def load_progress(progress_file: str) -> Tuple[set, Dict[str, List[Dict]]]:
    """Carga el progreso previo desde archivo si existe"""
    if os.path.exists(progress_file):
        try:
            with open(progress_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                processed_stations = set(data.get('processed_stations', []))
                grouped_data = defaultdict(list, data.get('grouped_data', {}))
                return processed_stations, grouped_data
        except Exception as e:
            logger.warning(f"Error al cargar progreso previo: {e}")
    return set(), defaultdict(list)

def save_progress(progress_file: str, processed_stations: set, grouped_data: Dict[str, List[Dict]]):
    """Guarda el progreso actual"""
    try:
        progress_data = {
            'processed_stations': list(processed_stations),
            'grouped_data': grouped_data
        }
        with open(progress_file, 'w', encoding='utf-8') as f:
            json.dump(progress_data, f, ensure_ascii=False)
    except Exception as e:
        logger.error(f"Error al guardar progreso: {e}")

def process_station(station_name: str, station_code: str, 
                   encoded_init_date: str, encoded_end_date: str) -> Optional[Dict]:
    """Procesa una estación individual con timeout"""
    start_time = time.time()
    retries = 0
    
    while retries < MAX_RETRIES:
        try:
            result = fetch_station_data(
                encoded_init_date,
                encoded_end_date,
                station_code
            )
            return result
            
        except Exception as e:
            retries += 1
            elapsed = time.time() - start_time
            if elapsed >= STATION_TIMEOUT:
                logger.warning(f"Timeout para estación {station_name} (intento {retries})")
                return None
                
            sleep_time = min(REQUEST_DELAY * retries, STATION_TIMEOUT - elapsed)
            logger.info(f"Reintentando estación {station_name} (intento {retries}) en {sleep_time:.1f}s")
            time.sleep(sleep_time)
    
    logger.warning(f"Falló después de {MAX_RETRIES} intentos para estación {station_name}")
    return None

def historical_data() -> Dict[str, List[Dict]]:
    """Obtiene la información histórica de las estaciones de meteorología de la AEMET - España"""
    try:
        # 1. Configuración inicial
        script_dir = os.path.dirname(__file__)
        progress_file = os.path.join(script_dir, 'json', 'progress.json')
        output_file = os.path.join(script_dir, 'json', 'weather_data.json')

        # 2. Obtener códigos de estaciones
        logger.info("Obteniendo códigos de estaciones EMA")
        obtain_stations_EMA_code()

        # Leer los códigos de las estaciones desde JSON
        json_path = os.path.join(script_dir, 'json', 'ema_codes.json')

        with open(json_path, 'r', encoding='utf-8') as archive:
            ema_codes = json.load(archive)

        # 3. Cargar progreso previo
        processed_stations, grouped_data = load_progress(progress_file)
        remaining_stations = {name: code for name, code in ema_codes.items() 
                            if name not in processed_stations}
        
        if not remaining_stations:
            logger.info("Todas las estaciones ya fueron procesadas anteriormente")
        else:
            logger.info(f"Estaciones por procesar: {len(remaining_stations)}/{len(ema_codes)}")

        # 4. Configurar rango de fechas
        encoded_init_date = DEFAULT_START_DATE.replace(':', '%3A')
        now = datetime.now(timezone.utc)
        end_date_str = now.strftime('%Y-%m-%dT%H:%M:%S') + 'UTC'
        encoded_end_date = end_date_str.replace(':', '%3A')

        # 5. Procesar estaciones
        total = len(remaining_stations)
        for i, (station_name, station_code) in enumerate(remaining_stations.items(), 1):
            logger.info(f"[{i}/{total}] Procesando estación: {station_name}")
            
            result = process_station(
                station_name,
                station_code,
                encoded_init_date,
                encoded_end_date
            )
            
            if result:
                grouped_data[station_name].append(result)
                processed_stations.add(station_name)
            
            else:
                # Marcar estación como procesada pero sin datos
                processed_stations.add(station_name)
                # Agregar información sobre el estado de la estación
                grouped_data[station_name] = [{
                    'fecha': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S%z'),
                    'estado': 'sin_datos',
                    'mensaje': 'No hay datos que satisfagan esos criterios'
                }]
                
                # Guardar progreso periódicamente
                if i % 5 == 0 or i == total:
                    save_progress(progress_file, processed_stations, grouped_data)
            
            time.sleep(REQUEST_DELAY)

        # 6. Guardar resultados finales
        if grouped_data:
            with open(output_file, 'w', encoding='utf-8') as archive:
                json.dump(grouped_data, archive, ensure_ascii=False, indent=4)
            logger.info(f"Datos guardados en {output_file}")
            
            # Limpiar archivo de progreso si todo se completó
            if len(processed_stations) == len(ema_codes):
                try:
                    os.remove(progress_file)
                except Exception as e:
                    logger.warning(f"No se pudo eliminar archivo de progreso: {e}")
            
            return dict(grouped_data)
        else:
            logger.warning("No se obtuvieron datos válidos")
            return None
        
    except json.JSONDecodeError as e:
        logger.error(f"Error al procesar archivos JSON: {str(e)}")
    except Exception as e:
        logger.error(f"Error inesperado: {str(e)}", exc_info=True)

historical_data()