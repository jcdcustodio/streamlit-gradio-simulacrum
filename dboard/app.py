import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Data Dashboard")

file_data = st.file_uploader("Upload CSV file", type="csv")

if file_data is not None:
    df = pd.read_csv(file_data)

    # Preview content of uploaded data
    st.subheader("Data Preview")
    st.write(df.head())

    # Summarize data
    st.subheader("Data Summary")
    st.write(df.describe())

    # Filter data
    # For demonstration, consider unique values
    st.subheader("Filter Data")
    columns = df.columns.tolist()
    select_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[select_column].unique()
    select_value = st.selectbox("Select value", unique_values)

    # Preview filter and plot result
    filtered_data = df[df[select_column] == select_value]
    st.write(filtered_data)

    st.subheader("Plot Data")
    st.text("Based on filter")
    colX = st.selectbox("Select X-axis column", columns)
    colY = st.selectbox("Select Y-axis column", columns)

    if st.button("Generate Plot"):
        try:
            st.line_chart(filtered_data.set_index(colX)[colY])
        except KeyError:
            st.text("Invalid plot parameters")
else:
    st.text("Waiting on file upload")