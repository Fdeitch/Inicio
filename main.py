import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(layout="wide")



df_reviews = pd.read_csv("Datasets/campeonato-brasileiro-gols.csv")
df_reviews
