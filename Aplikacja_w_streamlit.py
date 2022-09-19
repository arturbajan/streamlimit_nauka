import streamlit as st
import tools


st.header("Witaj w aplikacji analitycznej")
st.write("Możesz wybrać plik csv do analizy")


plik = st.file_uploader('Wybierz CSV')

try:
	if st.button("Pokaż CSV"):

		st.dataframe(tools.read_csv(plik))


	if st.button("Pokaż średnią wynagrodzeń"):
		
		c1, c2 = tools.avrg_difference(plik, "US", "GB")
		st.write("Country1:", c1)
		st.write("Country2:", c2)

except ValueError:

	st.write("Nie wybrałeś pliku")