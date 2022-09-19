import streamlit as st
from tools  import *
import pandas as pd

st.header("Witaj w aplikacji analitycznej")
st.write("Możesz wybrać plik csv do analizy")

plik = st.file_uploader('Wybierz CSV')

try:
	if st.button("Pokaż CSV"): 
		
		st.dataframe(tools.read_cvs(plik))
		#df = pd.read_csv(plik)

		#st.dataframe(df)

except ValueError:

	st.write("Nie wybrałeś pliku")
