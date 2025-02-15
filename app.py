#import streamlit as st
import pandas as pd

#st.set_page_config(layout="wide")"""

df_gols = pd.read_csv("campeonato-brasileiro-gols.csv")
df_gols["minuto"] = pd.to_numeric(df_gols["minuto"], errors='coerce')
above_74 = df_gols[df_gols["minuto"] > 74]
above_74.reset_index(drop=True, inplace=True)
above_74.describe()
above_74

