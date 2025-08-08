from datetime import datetime
import streamlit as st
import pandas as pd

caminho_datasets= "datasets"

df_compras=pd.read_csv(f"{caminho_datasets}/compras.csv", sep=";", decimal=",", index_col= 0)
df_lojas = pd.read_csv(f"{caminho_datasets}/lojas.csv",sep=";",decimal=",")
df_produtos = pd.read_csv(f"{caminho_datasets}/produtos.csv",sep=";",decimal=",")

df_lojas["estado/cidade"] = df_lojas["estado"] + "/" + df_lojas["cidade"]
#df_lojas["cidade/estado"]= df_lojas["cidade"] + "/" +  df_lojas["estado"]
lista_lojas = df_lojas["estado/cidade"].to_list()
loja_selecionada= st.sidebar.selectbox("Selecione uma loja: ", lista_lojas)

lista_vendedores = df_lojas.loc[df_lojas["estado/cidade"]== loja_selecionada,"vendedores"].iloc[0]

lista_vendedores= lista_vendedores.strip("][").replace("'", "").split(",")
#st.write(lista_vendedores)

vendedor_selecionado= st.sidebar.selectbox("Selecione o vendedor : ", lista_vendedores)

lista_produtos= df_produtos["nome"].to_list()

produto_selecionado= st.sidebar.selectbox("Selecione o produto :", lista_produtos)

nome_cliente= st.sidebar.text_input("Nome do cliente")
genero_selecionado = st.sidebar.selectbox("Genero do cliente",["masculino","feminino"])

forma_pagamento_selecionado= st.sidebar._selectbox("Forma de pagamento : ",["cartão de credito", "cartão de débito","PIX","dinheiro"])


if st.sidebar.button("Adicionar compra"):
    lista_adicionar= [df_compras["id_compra"].max() + 1 if not df_compras.empty else 1,
                      loja_selecionada,
                      vendedor_selecionado,
                      produto_selecionado,
                      nome_cliente,
                      genero_selecionado,
                      forma_pagamento_selecionado
                      ]
    df_compras.loc[datetime.now()]= lista_adicionar
    df_compras.to_csv(f"{caminho_datasets}/compras.csv", index=False,sep=";", decimal=",")
    
    st.success("Compra adicionada")
    
st.dataframe(df_compras)
    
    
