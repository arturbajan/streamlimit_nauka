import streamlit as st
import pandas as pd

df=pd.read_csv("https://stooq.pl/q/d/l/?s=eurpln&i=d")
df1=df[["Data","Otwarcie"]].set_index("Data").sort_index(ascending=False)
#df1.plot()
st.pyplot(df1)
