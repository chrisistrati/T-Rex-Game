import streamlit as st
import pandas as pd

st.title("Graphs and Data")
df=pd.read_csv("T-Rex Scores.csv")
st.header("Score over time")
st.line_chart(df["Score"], x_label="Time", y_label="Scores", color="#A52A2A")
st.divider()
st.header("Times run")
st.bar_chart(df["Date"].value_counts(), y_label="Times run", x_label="Date", color="#A52A2A",)