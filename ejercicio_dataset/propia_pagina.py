import pandas as pd
from .normalize_functions import *

#1. Which industry pays the most?
def part1():
    # Leo el excel
    rdf = pd.read_excel('Ask_A_Manager_Salary_Survey_2021.xlsx', engine='openpyxl')

    # Columna time_stamp
    time_stamp_df = rdf.iloc[:, 0]

    # Columna age_range
    age_range_df = rdf.iloc[:, 1]

    # Columna con el rango normalizado age_range_id
    age_range_id_df = normalize_age_range(age_range_df)

    # Columna indrustries
    industries_df = rdf.iloc[:,2]

    # Columna normalized_industries
    normalized_industries_df = normalize_industries(industries_df)

    #unir todos los dataframe
    final_df = pd.concat([
        time_stamp_df,
        age_range_df,
        age_range_id_df,
         industries_df,
         normalized_industries_df
    ], axis=1)

    final_df.columns = ['time_stamp', 'age_range', 'age_range_id', 'work_industries', 'normalized_industries']

    # almacenar los dataframe en un txt
    with open("clean_df.txt", "w", encoding='utf-8') as file:
        file.write(final_df.to_string(index=False))
        
    file.close()

    """ cleaned_df.columns = [
        'job_title',
        'job_context',
        'anual_salary',
        'aditional_monetary',
        'currency',
        'other_currency',
        'income_context',
        'country',
        'usa_state',
        'work_city',
        'total_experience_years',
        'field_experience_years',
        'educational_level',
        'gender',
        'race'
        ] """
    """  

    

    patronAcademic = r'^academic[-/\s]+(.*)'
    patronAdmin = r'administration[-/\s]+(.*)'
    patronAerospace = r'aerospace[-/\s]+(.*)'
    patronArchaeology = r'archaeology[-/\s]+(.*)'

    my_df = normalize(my_df=my_df, mask=mask_academic, regex=patronAcademic)
    my_df = normalize(my_df=my_df, mask=mask_admin, regex=patronAdmin)
    my_df = normalize(my_df=my_df, mask=mask_aerospace, regex=patronAerospace)
    my_df = normalize(my_df=my_df, mask=mask_archaeology, regex=patronArchaeology)

    # Obtener industria base y agrupar
    my_df['Industries'] = my_df['Industries'].str.extract(r'^\s*([^-/\s]+)', expand=False)
    df_resultado = (
        my_df.assign(specialization_temp=my_df['specialization'].fillna('N/A'))
        .groupby(['Industries', 'specialization_temp'])['Anual Salary']
        .sum()
        .reset_index()
        .rename(columns={'specialization_temp': 'specialization'})
    )

    with open("clean_df.txt", "w", encoding='utf-8') as file:
        file.write(df_resultado.to_string(index=False))
        
    file.close() """

    #print(df_resultado)


part1()
 

#2. How does salary increase given years of experience? 

#3. How do salaries compare for the same role in different locations? 

#4. How much do salaries differ by gender and years of experience? 

#5. How do factors like race and education level correlate with salary? 

#6. Is there a “sweet spot” total work experience vs years in the specific field? 