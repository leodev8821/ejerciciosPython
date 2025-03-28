import pandas as pd
from rapidfuzz import process, fuzz
import json
import os

# Normaliza el rango de edad
# Return --> Un DF con una columna 'age_range_id' y su id equivalente
def normalize_age_range(df):
    # Si es serie, lo convierto a DF
    if isinstance(df, pd.Series):
        df = df.to_frame()
    # Extraigo el nombre de la columna del DF
    column_name = df.columns[0]
    
    # mapeo de los rangos de edad con su id
    age_mapping = {
        'under 18': 1,
        '18-24': 2,
        '25-34': 3,
        '35-44': 4,
        '45-54': 5,
        '55-64': 6,
        '65 or over': 6
    }
    # Renombro la columna con el de 'age_range_id'
    df = df.rename(columns={column_name: 'age_range_id'})

    # Voy creando a partir de reemplazar valores en el nuevo DF
    with pd.option_context('future.no_silent_downcasting', True):
        df['age_range_id'] = df['age_range_id'].replace(age_mapping)

    return df

def normalize_industries(df):
    if isinstance(df, pd.Series):
        df = df.to_frame(name='normalized_industries')
    elif isinstance(df, pd.DataFrame):
        df = df.iloc[:, 0].to_frame('normalized_industries')
    else:
        raise ValueError("El parámetro debe ser un Series o DataFrame de pandas")
    
    df['normalized_industries'] = df['normalized_industries'].apply(normalize_text)
    return df

def normalize_text(text):
    script_dir = os.path.dirname(__file__)
    json_path = os.path.join(script_dir, 'json_patterns', 'industries.json')
        
    with open(json_path, 'r', encoding='utf-8') as archive:
        replacement_groups = json.load(archive)

    if pd.isna(text) or not isinstance(text, str):
        return 'unknown'
    
    text = text.strip().lower()
    if not text:
        return 'unknown'
    
    for replacement, targets in replacement_groups.items():
        result = process.extractOne(
            text,
            targets,
            processor=None
        )
        if result is None:
            continue
            
        best_match, score, _ = result
        if score >= 90:
            return replacement
            
    return 'other'