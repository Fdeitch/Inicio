import streamlit as st
import pandas as pd
#import plotly.express as px


st.set_page_config(layout="wide")

df_gols = pd.read_csv("APPWEB/campeonato-brasileiro-gols.csv")
df_gols["minuto"] = pd.to_numeric(df_gols["minuto"], errors='coerce')
above_74 = df_gols[df_gols["minuto"] > 74]
above_74

