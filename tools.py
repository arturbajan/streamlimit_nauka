import pandas as pd

def read_csv(plik):

	df = pd.read_csv(plik)
	df = df[['work_year','experience_level','employment_type','job_title','salary_in_usd','employee_residence','remote_ratio','company_location','company_size' ]]
	
	return df

def avrg_difference(plik, country1, country2):
	
	df = read_csv(plik)
	df_country1 = df[df['employee_residence'] == country1]
	df_country2 = df[df['employee_residence'] == country2]
	
	print(df_country1)
	print(df_country2)

	return df_country1['salary_in_usd'].mean(), df_country2['salary_in_usd'].mean()

