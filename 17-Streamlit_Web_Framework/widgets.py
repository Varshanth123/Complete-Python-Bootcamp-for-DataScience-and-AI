# Widgets are interactive UI elements in Streamlit (like buttons, sliders, and text inputs)
# that let users control your app without writing HTML or defining backend routes.

import streamlit as st
import pandas as pd
import csv
import os

st.title("Streamlit Text Input")

# Widgets
name = st.text_input("Enter your name:")

age = st.slider(
    "Select your age",
    0, 100, 25
)  # min value, max value, default value

location = st.text_input("Enter your Location Preference")

options = ["Python", "Java", "C", "C++", "JavaScript"]
lang = st.selectbox("Choose Your Preferred Language:", options)

# Display values
if name:
    st.write(f"Hello {name}")

st.write(f"Your age is {age}")
st.write(f"Your Location Preference is {location}")
st.write(f"Your Preferred Language: {lang}")

# Create CSV only if it doesn't exist
if not os.path.exists("sampledata.csv"):
    data = {
        "Name": ["Varshanth", "Sunny", "Skandha", "Sai"],
        "Age": [22, 20, 1, 30],
        "City": ["HYD", "SDNR", "Himayat Sagar", "Himayat Sagar"],
        "Language": ["Java", "C", "Python", "Python"],
    }

    df = pd.DataFrame(data)
    df.to_csv("sampledata.csv", index=False)

# Save new data only when button is clicked
if st.button("Save Data"):
    if name and location:
        new_row = [name, age, location, lang]

        with open("sampledata.csv", mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(new_row)

        st.success("Data saved successfully!")
    else:
        st.warning("Please enter your name and location.")

# Upload CSV
uploaded_file = st.file_uploader("Choose a CSV file:", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)