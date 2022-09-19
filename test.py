'''import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("https://stooq.pl/q/d/l/?s=eurpln&i=d")
df1=df[["Data","Otwarcie"]].set_index("Data").sort_index(ascending=False)
#df1.plot()
st.pyplot(df1)
'''


import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
