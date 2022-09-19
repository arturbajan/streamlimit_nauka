'''import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("https://stooq.pl/q/d/l/?s=eurpln&i=d")
df1=df[["Data","Otwarcie"]].set_index("Data").sort_index(ascending=False)
#df1.plot()
st.pyplot(df1)
'''
import streamlit as st
import pandas as pd
import numpu as np
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)
