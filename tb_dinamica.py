from datetime import datetime
from datetime import date, timedelta
import streamlit as st
import pandas as pd

caminho_datasets= "datasets"

PERC_COMISSAO= 0.05
COLUNAS_ANALISE=["loja","vendedor","produto","cliente_genero","forma_pagamento"]
COLUNAS_NUMERICAS=["preco","comissao"]
FUNCOES_AGREGACAO={"soma":"sum","contagem":"count"}

df_compras=pd.read_csv(f"{caminho_datasets}/compras.csv", sep=";", decimal=",", index_col= 0, parse_dates=True)
df_lojas = pd.read_csv(f"{caminho_datasets}/lojas.csv",sep=";",decimal=",")
df_produtos = pd.read_csv(f"{caminho_datasets}/produtos.csv",sep=";",decimal=",")

df_produtos=df_produtos.rename(columns={"nome":"produto"})
df_compras= df_compras.reset_index()
df_compras= pd.merge(
    left=df_compras,
    right=df_produtos[["produto","preco"]],
    on="produto",
    how="left"
    
   )
df_compras= df_compras.set_index("data")

df_compras["comissao"]= df_compras["preco"] * PERC_COMISSAO

indice_dinamico= st.sidebar.multiselect("Selecione os indices",COLUNAS_ANALISE)
colunas_filtradas=[c for c in COLUNAS_ANALISE if not c in indice_dinamico]

valor_analise = st.sidebar.selectbox("Selecione o valor",COLUNAS_NUMERICAS)
coluna_dinamica=st.sidebar.multiselect("Selecione as colunas", colunas_filtradas)
metrica_analise=st.sidebar.selectbox("Selecionar a métrica",list(FUNCOES_AGREGACAO.keys()))

if len(indice_dinamico) > 0 and len(coluna_dinamica) > 0 :
    metrica = FUNCOES_AGREGACAO[metrica_analise]
    compras_dinamicas= pd.pivot_table(
        df_compras,
        index=indice_dinamico,
        columns= coluna_dinamica,
        values=valor_analise,
        aggfunc= metrica

        )
    compras_dinamicas["TOTAL_GERAL"]= compras_dinamicas.sum(axis=1)
    compras_dinamicas.loc["TOTAL_GERAL"]= compras_dinamicas.sum(axis=0).to_list()
    st.dataframe(compras_dinamicas)

