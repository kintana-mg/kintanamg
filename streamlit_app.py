import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Data visualisation from a csv file.")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:", df.head())

    x_column = st.selectbox("Select X Column", df.columns)
    y_column = st.selectbox("Select Y Column", df.columns)

    if st.button("Plot"):
        x = df[x_column]
        y = df[y_column]
        
        # Frequency analysis logic here
        plt.figure()
        plt.plot(x, y, "o")
        plt.title("Frequency Analysis")
        plt.xlabel("Frequency")
        plt.ylabel("Power")
        st.pyplot(plt)
