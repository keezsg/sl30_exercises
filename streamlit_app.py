import streamlit as st
import numpy as np
import altair as alt
import pandas as pd

#st.write("Hello world!")
#if st.button('Say hello'):
#   st.write('Why hello there')
#else:
#   st.write("Goodbye")

st.header('st.write')

#example 1
st.write("Hello, *World!* : sunglasses1:")

st.write(1234)

df = pd.DataFrame(
        {
        'A': [1,2,3,4],
        'B': [10,20,30,40],
        }
)

st.write(df)

df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns=['a', 'b', 'c']
)

c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
