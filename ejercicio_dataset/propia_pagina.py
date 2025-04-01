import pandas as pd
from .normalize_functions import *

#1. Which industry pays the most?
def part1():
    # Leo el excel
    rdf = pd.read_excel('Ask_A_Manager_Salary_Survey_2021.xlsx', engine='openpyxl')

    # Columna 0 time_stamp
    time_stamp_df = rdf.iloc[:, 0]

    # Columna 1 age_range
    age_range_df = rdf.iloc[:, 1].fillna('no_data')

    # Columna 2 con el rango normalizado age_range_id
    age_range_id_df = normalize_age_range(age_range_df)

    # Columna 3 indrustries
    industries_df = rdf.iloc[:,2].fillna('no_data')

    # Columna 4 normalized_industries
    normalized_industries_df = normalize_text(industries_df,'normalized_industries',1)

    # Columna 5 job_title
    job_title_df = rdf.iloc[:,3].fillna('no_data')

    # Columna 6 job_title_context
    job_title_context_df = rdf.iloc[:,4].fillna('no_data')

    # Columna 7 anual_salary
    anual_salary_df = rdf.iloc[:,5].fillna(0)

    # Columna 8 aditional_monetary
    aditional_monetary_df = rdf.iloc[:,6].fillna(0)

    # Columna 9 currency
    currency_df = rdf.iloc[:,7].fillna('no_data')

    # Columna 10 con el rango normalizado currency_id
    currency_id_df = normalize_currency(currency_df)

    # Columna 11 con other_currencies
    other_currency_df = rdf.iloc[:,8].fillna('no_data')

    # Columna 12 con el rango normalizado other_currency_id
    other_currency_id_df = normalize_text(other_currency_df,'other_currencies_id',2)

    # Columna 13 income_context
    income_context_df = rdf.iloc[:,9].fillna('no_data')

    # Columna 13 work_country
    work_country_df = rdf.iloc[:,10].fillna('no_data')

    # Columna 14 normalized_work_country
    normalized_work_country_df = normalize_text(work_country_df,'normalized_work_country',3)

    # Columna 15 work_country
    us_states_df = rdf.iloc[:,11].fillna('no_data')

    # Columna 16 normalized_work_country
    normalized_us_states_df = normalize_text(us_states_df,'normalized_us_states',4)

    # Columna 17 us_work_city
    us_work_city_df = rdf.iloc[:,12].fillna('no_data')

    # Columna 18 overall_work_experience
    overall_work_experience_df = rdf.iloc[:,13].fillna('no_data')

    # Columna 19 con el rango normalizado overall_work_experience_id
    overall_work_experience_id_df = normalized_work_experience(overall_work_experience_df)

    # Columna 20 overall_work_experience
    field_work_experience_df = rdf.iloc[:,14].fillna('no_data')

    # Columna 21 con el rango normalizado field_work_experience_id
    field_work_experience_id_df = normalized_work_experience(field_work_experience_df)

    # Columna 22 highest_education_level
    highest_education_level_df = rdf.iloc[:,15].fillna('no_data')

    # Columna 23 con el rango normalizado highest_education_level_id
    highest_education_level_id_df = normalized_highest_education_level(highest_education_level_df)

    # Columna 24 gender
    gender_df = rdf.iloc[:,16].fillna('no_data')

    # Columna 23 con el rango normalizado gender_id
    gender_id_df = normalized_gender(gender_df)

    # Columna 25 race
    race_df = rdf.iloc[:,17].fillna('no_data')

    #unir todos los dataframe
    final_df = pd.concat([
        time_stamp_df,
        age_range_id_df,
        age_range_df,
        normalized_industries_df,
        industries_df,
        job_title_df,
        job_title_context_df,
        anual_salary_df,
        aditional_monetary_df,
        currency_id_df,
        currency_df,
        other_currency_id_df,
        other_currency_df,
        income_context_df,
        normalized_work_country_df,
        work_country_df,
        normalized_us_states_df,
        us_states_df,
        us_work_city_df,
        overall_work_experience_id_df,
        overall_work_experience_df,
        field_work_experience_id_df,
        field_work_experience_df,
        highest_education_level_id_df,
        highest_education_level_df,
        gender_id_df,
        gender_df,
        race_df
    ], axis=1)

    final_df.columns = [
        'time_stamp', 
        'age_range_id', 
        'age_range', 
        'normalized_industries', 
        'work_industries', 
        'job_title', 
        'job_title_context',
        'anual_salary',
        'aditional_monetary',
        'currency_id',
        'currency',
        'other_currency_id',
        'other_currency',
        'income_context',
        'normalized_work_country',
        'work_country',
        'normalized_us_states',
        'us_states',
        'us_work_city',
        'overall_work_experience_id',
        'overall_work_experience',
        'field_work_experience_id',
        'field_work_experience',
        'highest_education_level_id',
        'highest_education_level',
        'gender_id',
        'gender',
        'race'
        ]

    #almacenar los dataframe en un txt
    with open("clean_df.txt", "w", encoding='utf-8') as file:
         file.write(final_df.to_string(index=False))
        
    file.close()

    # Si el Excel no existe, lo crea
    # if not os.path.exists('normalized_answer.xlsx'):
    #     with pd.ExcelWriter('normalized_answer.xlsx',mode='w',engine='openpyxl') as writer:
    #         final_df.to_excel(
    #             writer,
    #             sheet_name='normalized_answer',
    #             index=False
    #         )

    # # Obtener industria base y agrupar
    # my_df['Industries'] = my_df['Industries'].str.extract(r'^\s*([^-/\s]+)', expand=False)
    # df_resultado = (
    #     my_df.assign(specialization_temp=my_df['specialization'].fillna('N/A'))
    #     .groupby(['Industries', 'specialization_temp'])['Anual Salary']
    #     .sum()
    #     .reset_index()
    #     .rename(columns={'specialization_temp': 'specialization'})
    # )

part1()


#2. How does salary increase given years of experience? 

#3. How do salaries compare for the same role in different locations? 

#4. How much do salaries differ by gender and years of experience? 

#5. How do factors like race and education level correlate with salary? 

#6. Is there a “sweet spot” total work experience vs years in the specific field? 