import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Amanuel Dashboard", page_icon="👋")


tab = st.sidebar.radio("Navigate", ["Home", "Project", "Data"])
st.sidebar.success("Select a tab above.")


if tab == "Home":
    st.title("Welcome to Amanuel Dashboard")
    st.caption("Simple Streamlit layout with widgets, a table, and a chart using synthetic data.")

elif tab == "Project":
    st.header("Project")
    st.markdown(
        "This mini app shows a clear dashboard structure with unique widgets and readable visuals. "
        "It uses synthetic data to demonstrate layout and interaction."
    )

   
    st.subheader("Aim")
    st.markdown(
        """
        The aim of this project is to *develop an interactive dashboard capable of predicting the likelihood of heart disease*
        using health-related parameters such as age, blood pressure, cholesterol level, glucose level, and other clinical risk factors.
        The dashboard is designed to visualize patient data, enable real-time exploration of predictors, and support informed
        decision-making for early detection and prevention of cardiovascular conditions.
        """
    )

elif tab == "Data":
    st.header("Health Monitoring (Synthetic)")

    # --- Three widgets ---
    c1, c2, c3 = st.columns(3)
    with c1:
        base_hr = st.number_input("Resting Heart Rate (bpm)", 40, 200, 72)
    with c2:
        water = st.slider("Water Intake (liters)", 0.0, 5.0, 2.0, 0.1)
    with c3:
        activity = st.selectbox("Activity Type", ["Resting", "Walking", "Running", "Cycling"])

    # --- Data generation ---
    @st.cache_data
    def make_data(n, base_hr, water, activity):
        rng = np.random.default_rng(42)
        boost = {"Resting": 0, "Walking": 8, "Running": 25, "Cycling": 15}[activity]
        var = max(1.0, 6.0 - 0.5 * water)
        x = np.arange(n)
        hr = base_hr + boost + rng.normal(0, var, n)
        return pd.DataFrame({"Minute": x, "HeartRate": hr.round().astype(int), "Activity": activity})

    df = make_data(120, base_hr, water, activity)

    # --- Chart ---
    st.subheader("Heart Rate Over Time")
    st.plotly_chart(
        px.line(df, x="Minute", y="HeartRate", title=f"Heart Rate — {activity}", markers=True),
        use_container_width=True
    )

    # --- Table + download ---
    st.subheader("Synthetic Data")
    st.dataframe(df, use_container_width=True)
    st.download_button(
        "Download CSV",
        df.to_csv(index=False).encode("utf-8"),
        "health_monitoring_synthetic.csv",
        "text/csv"
    )