import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Amanuel Dashboard",
    page_icon="👋",
)

# Sidebar configuration
st.sidebar.image("./assets/project-logo.jpg",)
tab = st.sidebar.radio(
    "Navigate",
    ["Home", "Project", "Data"]
)
st.sidebar.success("Select a tab above.")

# # Page information
if tab == "Home":
    st.write("# Welcome to Amanuel Dashboard!")
    st.write("## Aims:")
    st.markdown("""
        Different data visualizations and analyses. 
    """)

elif tab == "Project":
    st.write("## Project")
    st.markdown("""
        Developing of a machine learning model for predicting the survivability of colorectal cancer patients.
    """)
elif tab == "Data":
    import plotly.express as px

    @st.cache_data
    def get_data():
        df = pd.DataFrame(
            np.random.randn(50, 20), columns=("col %d" % i for i in range(20))
        )
        return df

    @st.cache_data
    def convert_for_download(df):
        return df.to_csv().encode("utf-8")

    df = get_data()
    csv = convert_for_download(df)

    st.download_button(
    label="Download CSV",
    data=csv,
    file_name="data.csv",
    mime="text/csv",
    icon=":material/download:",
    )
    @st.cache_data
    def get_data():
        df = pd.DataFrame(
            np.random.randn(50, 2), columns=["Smoking", "Cancer risk"]
        )
        return df
    df = get_data()
    st.write("## Interactive Plot")
    fig = px.scatter(df, x="Smoking", y="Cancer risk", title="Cancer Risk Scatter Plot")
    st.plotly_chart(fig, use_container_width=True)

    st.write("## Aquired Data")
    st.dataframe(df)

    add_slider = st.slider(
        'Select a range of values',
        0.0, 100.0, (25.0, 75.0)
    )