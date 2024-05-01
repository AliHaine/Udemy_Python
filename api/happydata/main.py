import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv("happy.csv")

st.title("In Search for Happiness")
xAxis = st.selectbox("Select the data for the X-axis", df.columns)
yAxis = st.selectbox("Select the data for the Y-axis", df.columns)

figure = px.scatter(x=df[xAxis], y=df[yAxis], labels={"x": xAxis, "y": yAxis})
st.plotly_chart(figure)
