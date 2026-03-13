#%%

import pandas as pd
import numpy as np
df = pd.read_csv("../../data/transacoes.csv", sep=";")

df_cl = pd.read_csv("../../data/clientes.csv", sep=";") 
df_cl
#%%

#05.05 - Selecione a primeira transação diária de cada cliente.


df = df.sort_values("DtCriacao")
df["data"] = pd.to_datetime(df["DtCriacao"]).dt.date
df
# %%

first = df.drop_duplicates(keep="first", subset=["IdCliente", "data"])
last = df.drop_duplicates(keep="last", subset=["IdCliente", "data"])

pd.concat([last, first])

#%%
# Crie uma coluna nova “twitch_points” 
# que e resultado da multiplicação do saldo de pontos e a marcação da twitch


df_cl["twitch_points"] = df_cl["qtdePontos"] * df_cl["flTwitch"]
df_cl.head()

#%%

# Aplique o log na coluna de saldo de pontos, criando uma coluna nova

df_cl["Pontos_Log"] = np.log(df_cl["qtdePontos"])
df_cl.head()

#%%
# 05.03 - Crie uma coluna que sinalize se a
# pessoa tem vínculo com alguma (qualquer uma)
# plataforma de rede social.

df_cl["plataformas"] =(df_cl["flEmail"]+df_cl["flTwitch"]+df_cl["flYouTube"]+df_cl["flBlueSky"]+df_cl["flInstagram"])
df_cl

#%%
# 05.04 - Qual é o id de cliente que tem maior saldo de pontos?


df_cl.sort_values("qtdePontos", ascending=False).head(5)[["idCliente","qtdePontos"]]

#%%
# E o menor?



(df_cl.sort_values("qtdePontos", ascending=True)
    .head(5)[["idCliente","qtdePontos"]])

