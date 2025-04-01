import pandas as pd
from rapidfuzz import process, fuzz, utils
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
        '65 or over': 7
    }
    # Renombro la columna con el de 'age_range_id'
    df = df.rename(columns={column_name: 'age_range_id'})

    # Voy creando a partir de reemplazar valores en el nuevo DF
    with pd.option_context('future.no_silent_downcasting', True):
        df['age_range_id'] = df['age_range_id'].replace(age_mapping)

    return df

# Normaliza el rango de experiencia en años
# Return --> Un DF con una columna 'overall_experience_years_id' y su id equivalente
def normalized_work_experience(df):
    # Si es serie, lo convierto a DF
    if isinstance(df, pd.Series):
        df = df.to_frame()
    # Extraigo el nombre de la columna del DF
    column_name = df.columns[0]
    
    # mapeo de los rangos de edad con su id
    experience_mapping = {
        "1 year or less" : 1,
        "2 - 4 years" :	2,
        "5-7 years" : 3,
        "8 - 10 years" : 4,
        "11 - 20 years" : 5,
        "21 - 30 years" : 6,
        "31 - 40 years" : 7,
        "41 years or more" : 8
    }
    # Renombro la columna con el de 'age_range_id'
    df = df.rename(columns={column_name: 'experience_years_id'})

    # Voy creando a partir de reemplazar valores en el nuevo DF
    with pd.option_context('future.no_silent_downcasting', True):
        df['experience_years_id'] = df['experience_years_id'].replace(experience_mapping)

    return df

# Normaliza el rango de estudios
# Return --> Un DF con una columna 'highest_education_level_id' y su id equivalente
def normalized_highest_education_level(df):
    # Si es serie, lo convierto a DF
    if isinstance(df, pd.Series):
        df = df.to_frame()
    # Extraigo el nombre de la columna del DF
    column_name = df.columns[0]
    
    # mapeo de los rangos de edad con su id
    education_mapping = {
        "no_data" : 0,
        "High School" : 1,
        "Some college" : 2,
        "College degree" : 3,
        "Master's degree" : 4,
        "Professional degree (MD, JD, etc.)" : 5,
        "PhD" : 6
    }
    # Renombro la columna con el de 'age_range_id'
    df = df.rename(columns={column_name: 'highest_education_level_id'})

    # Voy creando a partir de reemplazar valores en el nuevo DF
    with pd.option_context('future.no_silent_downcasting', True):
        df['highest_education_level_id'] = df['highest_education_level_id'].replace(education_mapping)

    return df

# Normaliza el rango de genero
# Return --> Un DF con una columna 'gender_id' y su id equivalente
def normalized_gender(df):
    # Si es serie, lo convierto a DF
    if isinstance(df, pd.Series):
        df = df.to_frame()
    # Extraigo el nombre de la columna del DF
    column_name = df.columns[0]
    
    # mapeo de los rangos de edad con su id
    gender_mapping = {
        "no_data" : 0,
        "Man": 1,
        "Woman": 2,
        "Non-binary": 3,
        "Other or prefer not to answer": 4,
        "Prefer not to answer": 4
    }
    # Renombro la columna con el de 'age_range_id'
    df = df.rename(columns={column_name: 'gender_id'})

    # Voy creando a partir de reemplazar valores en el nuevo DF
    with pd.option_context('future.no_silent_downcasting', True):
        df['gender_id'] = df['gender_id'].replace(gender_mapping)

    return df

# Normalizar los textos con los indicados en un json
def normalize_text(df, df_name, option):
    if isinstance(df, pd.Series):
        df = df.to_frame(name=df_name)
    elif isinstance(df, pd.DataFrame):
        df = df.iloc[:, 0].to_frame(df_name)
    else:
        raise ValueError("El parámetro debe ser un Series o DataFrame de pandas")
    
    match option:
        case 1:
            df[df_name] = df[df_name].apply(convert_industries_text)
        case 2:
            df[df_name] = df[df_name].apply(convert_currency_text)
            df = normalize_currency(df)
        case 3:
            df[df_name] = df[df_name].apply(convert_work_country_text)
        case 4:
            df[df_name] = df[df_name].apply(convert_us_states_text)

    return df

def convert_industries_text(text):
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


def convert_currency_text(text):
    script_dir = os.path.dirname(__file__)
    json_path = os.path.join(script_dir, 'json_patterns', 'other_currencies.json')
        
    with open(json_path, 'r', encoding='utf-8') as archive:
        replacement_groups = json.load(archive)

    if pd.isna(text) or not isinstance(text, str):
        return 'n/a'
    
    text = text.strip().lower()
    if not text:
        return 'n/a'
    
    for replacement, targets in replacement_groups.items():
        result = process.extractOne(
            text,
            targets,
            scorer=fuzz.WRatio,
            processor=utils.default_process
        )
        if result is None:
            continue
            
        best_match, score, _ = result
        if score >= 90:
            return replacement
            
    return 'other'

def convert_work_country_text(text):
    script_dir = os.path.dirname(__file__)
    json_path = os.path.join(script_dir, 'json_patterns', 'work_country.json')
        
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
        if score >= 80:
            return replacement
            
    return 'other'

def convert_us_states_text(text):
    script_dir = os.path.dirname(__file__)
    json_path = os.path.join(script_dir, 'json_patterns', 'us_states.json')
        
    with open(json_path, 'r', encoding='utf-8') as archive:
        replacement_groups = json.load(archive)

    if pd.isna(text) or not isinstance(text, str):
        return 'unknown'
    
    text = text.strip().lower()
    if not text:
        return 'n/a'
    
    for replacement, targets in replacement_groups.items():
        result = process.extractOne(
            text,
            targets,
            processor=None
        )
        if result is None:
            continue
            
        best_match, score, _ = result
        if score >= 80:
            return replacement
            
    return 'n/a'

# Normaliza el currency
# Return --> Un DF con una columna 'currency_id' y su id equivalente
def normalize_currency(df):
    # Si es serie, lo convierto a DF
    if isinstance(df, pd.Series):
        df = df.to_frame()
    # Extraigo el nombre de la columna del DF
    column_name = df.columns[0]
    
    # mapeo de los currency con su id
    script_dir = os.path.dirname(__file__)
    json_path = os.path.join(script_dir, 'json_patterns', 'currencies.json')
        
    with open(json_path, 'r', encoding='utf-8') as archive:
        replacement_groups = json.load(archive)

    # Renombro la columna con el de 'currency_id'
    df = df.rename(columns={column_name: 'currency_id'})

    # Voy creando a partir de reemplazar valores en el nuevo DF
    with pd.option_context('future.no_silent_downcasting', True):
        df['currency_id'] = df['currency_id'].replace(replacement_groups)
    return df