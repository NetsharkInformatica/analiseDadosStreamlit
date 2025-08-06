import random
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd
import names
import streamlit as st
import os

pasta_dataset = Path(__file__).parent / "datasets"

pasta_dataset.mkdir(parents=True , exist_ok=True)

LOJAS=[
     {
        "estado": "SP",
        "cidade": "São Paulo",
        "vendedores": ["João Silva", "Maria Oliveira", "Carlos Souza"]
    },
     {
        "estado": "RJ",
        "cidade": "Rio de Janeiro",
        "vendedores": ["Ana Costa", "Pedro Santos"]
    },
    {
        "estado": "MG",
        "cidade": "Belo Horizonte",
        "vendedores": ["Marcos Lima", "Fernanda Alves", "Ricardo Pereira"]
    },
     {
        "estado": "BA",
        "cidade": "Salvador",
        "vendedores": ["Patrícia Rocha", "Lucas Mendes"]
    },
     {
        "estado": "PR",
        "cidade": "Curitiba",
        "vendedores": ["Gustavo Schmidt", "Juliana Weber"]
    },
     {
        "estado": "SC",
        "cidade": "Florianópolis",
        "vendedores": ["Roberto Krause", "Camila Schultz"]
    },
    {
        "estado": "RS",
        "cidade": "Porto Alegre",
        "vendedores": ["Diego Gonçalves", "Tatiana Martins"]
    },
    {
        "estado": "PE",
        "cidade": "Recife",
        "vendedores": ["Felipe Albuquerque", "Vanessa Lopes"]
    },
    {
        "estado": "CE",
        "cidade": "Fortaleza",
        "vendedores": ["Raquel Dias", "Eduardo Nogueira"]
    },
    {
        "estado": "GO",
        "cidade": "Goiânia",
        "vendedores": ["Márcio Castro", "Simone Ribeiro", "André Luiz"]
    }
]

PRODUTOS=[
    {"id": 1, "nome": "Smartphone Galaxy S23", "preco": 4599.90},
    {"id": 2, "nome": "iPhone 15 Pro", "preco": 7599.00},
    {"id": 3, "nome": "Notebook Dell Inspiron 15", "preco": 3299.99},
    {"id": 4, "nome": "TV LED 55'' 4K Samsung", "preco": 2899.50},
    {"id": 5, "nome": "Fone de Ouvido Bluetooth Sony", "preco": 399.90},
    {"id": 6, "nome": "Tablet Amazon Fire HD 10", "preco": 1299.00},
    {"id": 7, "nome": "Smartwatch Xiaomi Mi Band 7", "preco": 299.00},
    {"id": 8, "nome": "Câmera Canon EOS R6", "preco": 12599.00},
    {"id": 9, "nome": "Console PlayStation 5", "preco": 3899.90},
    {"id": 10, "nome": "Xbox Series X", "preco": 3599.99},
    {"id": 11, "nome": "Monitor Gamer 27'' 144Hz", "preco": 1899.00},
    {"id": 12, "nome": "Teclado Mecânico RGB", "preco": 499.50},
    {"id": 13, "nome": "Mouse Gamer Sem Fio", "preco": 349.90},
    {"id": 14, "nome": "Impressora Multifuncional HP", "preco": 899.00},
    {"id": 15, "nome": "SSD 1TB NVMe", "preco": 599.99},
    {"id": 16, "nome": "Caixa de Som JBL Charge 5", "preco": 1099.00},
    {"id": 17, "nome": "Drone DJI Mini 3 Pro", "preco": 4999.00},
    {"id": 18, "nome": "Roteador Wi-Fi 6", "preco": 799.50},
    {"id": 19, "nome": "Webcam Full HD Logitech", "preco": 459.90},
    {"id": 20, "nome": "Smart Speaker Amazon Echo", "preco": 599.00}
]

FORMA_PGTO=["cartão de credito", "cartão de débito","PIX","dinheiro"]

GENERO_CLIENTES=["MALE","FEMALE"]
compras=[]

for _ in range(2000):
    loja = random.choice(LOJAS)
    vendedor = random.choice(loja["vendedores"])
    produto = random.choice(PRODUTOS)
    hora_compra = datetime.now() - timedelta(
        days=random.randint(1, 365),
        hours=random.randint(-5, 5),
        minutes=random.randint(-30, 30)
    )
    genero_cliente = random.choice(GENERO_CLIENTES)
    nome_cliente = names.get_full_name(genero_cliente)
    forma_pagto = random.choice(FORMA_PGTO)    
    compras.append({
        "data":hora_compra,
        "id_compra":0,
        "loja":loja["cidade"],
        "vendedor":vendedor,
        "produto":produto["nome"],
        "cliente_nome":nome_cliente,
        "cliente_genero":genero_cliente.replace("MALE","masculino").replace("FEMALE","feminino"),
        "forma_pgto":forma_pagto
    
    })

df_compras = pd.DataFrame(compras).set_index("data").sort_index()
df_compras["id_compra"]= [i for i in range(len(df_compras))]

df_lojas=pd.DataFrame(LOJAS)
#df_lojas["id_lojas"]=[l for l in range(len(loja))]

df_produtos=pd.DataFrame(PRODUTOS)


#exportando os dataframes


df_compras.to_csv(pasta_dataset / "compras.csv", decimal="," , sep=";")
#df_compras.to_csv(pasta_dataset / "compras.csv", decimal=",", sep=";")
df_lojas.to_csv(pasta_dataset / "lojas.csv",decimal=",", sep=";")
df_produtos.to_csv(pasta_dataset / "produtos.csv",decimal=",",sep=";")

#exportando em excel

df_compras.to_excel(pasta_dataset /"compras.xlsx")
df_lojas.to_excel(pasta_dataset / "lojas.xlsx")
df_produtos.to_excel(pasta_dataset / "produtos.xlsx")



    
    