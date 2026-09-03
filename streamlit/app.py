import numpy as np
import pandas as pd
import streamlit as st

# this is a title
st.title("hello streamlit")

# create a simple text 
st.write("this is a simple text")

# create a simple Dataframe

df = pd.DataFrame({
  'first column': [1,2,3,4],
  'second  column': [10, 20, 30, 40]
})

# Display the dataframe
st.write("Here is the dataframe")
st.write(df)

# create a line chart

char_data = pd.DataFrame(
  np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(char_data)