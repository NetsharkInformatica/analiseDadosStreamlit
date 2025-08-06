import streamlit as st
import pandas as pd
import os

caminho_compras = os.path.abspath("datasets/compras.csv")
#caminho_compras = "analisedadosstreamlit/datasets/compras.csv"  # Adicione o nome do arquivo
df_compras = pd.read_csv(caminho_compras, sep=";", decimal=",")
df_compras= pd.read_csv(caminho_compras, sep=";", decimal=",")

st.dataframe(df_compras) 

