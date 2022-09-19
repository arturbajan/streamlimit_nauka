import pandas as pd

def read_csv(plik):

	df = pd.read_csv(plik)
	df = df[['work_year','experience_level','employment_type','job_title','salary_in_usd','employee_residence','remote_ratio','company_location','company_size' ]]
