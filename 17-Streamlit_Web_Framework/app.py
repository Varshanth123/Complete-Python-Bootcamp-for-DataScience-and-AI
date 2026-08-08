# for executing use python -m streamlit run app.py
import streamlit as st
import pandas as pd
import numpy as np

## Ttle of the aplication 
st.title('Hello Streamlit')

## Display a simple text
st.write("This is a simple text")

## Create a simplete DataFrame
df =pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})

## Display the DataFrame
st.write("Here is the DataFrame")
st.write(df)

# Create a line chart

chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)

# np.random.randn(20, 3) → Generates a 20 × 3 array of random numbers 
# from a standard normal distribution (mean = 0, standard deviation = 1).

# pd.DataFrame(...) → Converts that array into a Pandas DataFrame (table).

# columns=['a', 'b', 'c'] → Names the three columns as a, b, and c.

st.line_chart(chart_data)
