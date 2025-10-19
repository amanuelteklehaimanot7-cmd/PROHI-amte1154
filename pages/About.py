import streamlit as st

st.title("Amanuel Teklehaimanot"
)
st.markdown(
"""
During the Data Science for Health Informatics (DSHI) course,
I developed a machine learning model to predict the likelihood
of heart disease using a combined Kaggle dataset of 918 patient
records and 16 clinical and demographic features, including age,
cholesterol level, chest pain type, and maximum heart rate. I 
performed data cleaning, exploratory data analysis, and feature
correlation studies, then evaluated several models—Logistic 
Regression, Decision Tree, and K-Nearest Neighbors (KNN). The
KNN model with k = 7 achieved the best F1-score, effectively
balancing precision and recall. Techniques such as normalization,
visualization, and model valuation were applied to improve
accuracy. This Streamlit dashboard summarizes the workflow and
provides an interactive structure that can be extended for health
data analysis and early disease risk detection.
"""
)