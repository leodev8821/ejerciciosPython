import pandas as pd

#1. Which industry pays the most?
def part1():
    # Leo el excel
    rdf = pd.read_excel('Ask_A_Manager_Salary_Survey_2021.xlsx', engine='openpyxl')

    # Extraigo las columnas 2 y 5 y les asigno un nombre en un nuevo dataframe
    my_df = rdf.iloc[:, [2, 5]].copy()
    my_df.columns = ['Industries', 'Anual Salary']

    #parámetros para reemplazar
    replacements = {
    'academia': 'academic',
    'administrative': 'administration',
    'archaeologist' : 'archaeology',
    '"Government Relations"' : 'Government Relations'
    }

    # Normalizar nombres de la columna 1
    my_df['Industries'] = (
        my_df['Industries']
        .str.strip()
        .str.lower()
        .replace(replacements, regex=True)
    )  

    # Extracción de especialización
    mask_academic = my_df['Industries'].str.contains(r'^academic[-/\s]+', regex=True, na=False)
    mask_admin = my_df['Industries'].str.contains(r'^administration[-/\s]+', regex=True, na=False)
    mask_aerospace = my_df['Industries'].str.contains(r'^aerospace[-/\s]+', regex=True, na=False)
    mask_archaeology = my_df['Industries'].str.contains(r'^archaeology[-/\s]+', regex=True, na=False)

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
        
    file.close()

    #print(df_resultado)


def normalize(my_df, mask, regex):
    my_df.loc[mask, 'specialization'] = (
        my_df.loc[mask, 'Industries']
        .str.extract(regex)[0]
        .fillna('')
        .str.lower()
        .str.replace(r'[\/\&]', ' ', regex=True)
        .str.replace(r'[^a-z\s]', '', regex=True)
        .str.replace('and', '')
        .str.replace(r'\s+', ' ', regex=True)
    )
    return my_df

part1()
 

#2. How does salary increase given years of experience? 

#3. How do salaries compare for the same role in different locations? 

#4. How much do salaries differ by gender and years of experience? 

#5. How do factors like race and education level correlate with salary? 

#6. Is there a “sweet spot” total work experience vs years in the specific field? 