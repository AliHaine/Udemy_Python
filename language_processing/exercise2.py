import pandas as pd
import streamlit as st
import plotly.express as px
import glob
from nltk.sentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

files = glob.glob("diary/*")
result = {}
for file in files:
    file_content = open(file).read()
    score = analyzer.polarity_scores(file_content)
    result[file[6:-4]] = score
dataframe = pd.DataFrame.from_dict(result)

st.title("Positivity")
figure = px.line(x=result.keys(), y=dataframe.loc['pos', :].values)
st.plotly_chart(figure)

st.title("Negativity")
figure = px.line(x=result.keys(), y=dataframe.loc['neg', :].values)
st.plotly_chart(figure)

