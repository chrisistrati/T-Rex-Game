import streamlit as st
import pandas as pd

st.title("T-Rex Bot Scores over time", )
df=pd.read_csv("T-Rex Scores.csv")
st.line_chart(df["Score"], x=None, x_label="Time", y_label="Scores", color="#A52A2A")
st.bar_chart(df["Score"].count())