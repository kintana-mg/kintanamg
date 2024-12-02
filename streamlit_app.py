import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Phase Fold and visualise lightcurves")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
if uploaded_file:
    # Read uploaded CSV
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:", df.head())

    # Column selection
    x_column = st.selectbox("Select Time Column (X)", df.columns)
    y_column = st.selectbox("Select Magnitude/Flux Column (Y)", df.columns)

    # Input for period in days
    period_days = st.number_input("Enter the period in days for phase folding:", min_value=0.0, step=0.1)

    if st.button("Analyze"):
        # Extract columns
        x = df[x_column]
        y = df[y_column]
        
        # Plot original lightcurve
        st.subheader("Original Lightcurve")
        plt.figure(figsize=(8, 4))
        plt.plot(x, y, 'o', markersize=2, label="Original Lightcurve")
        plt.xlabel("Time")
        plt.ylabel("Magnitude/Flux")
        plt.gca().invert_yaxis()  # Typical for magnitude plots
        plt.title("Original Lightcurve")
        plt.legend()
        st.pyplot(plt)

        # Check if a valid period is entered
        if period_days > 0:
            # Phase folding
            phase = (x % period_days) / period_days  # Compute phase
            sorted_indices = np.argsort(phase)  # Sort by phase
            phase = phase[sorted_indices]
            y = y[sorted_indices]

            # Plot phase-folded lightcurve
            st.subheader("Phase-Folded Lightcurve")
            plt.figure(figsize=(8, 4))
            plt.plot(phase, y, 'o', markersize=2, label="Phase-Folded Lightcurve")
            plt.xlabel("Phase")
            plt.ylabel("Magnitude/Flux")
            plt.gca().invert_yaxis()  # Typical for magnitude plots
            plt.title(f"Phase-Folded Lightcurve (Period = {period_days} days)")
            plt.legend()
            st.pyplot(plt)
        else:
            st.warning("Please enter a valid period in days to phase-fold the lightcurve.")
