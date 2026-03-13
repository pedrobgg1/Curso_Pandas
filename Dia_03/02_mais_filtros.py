#%%

import pandas as pd

dataf = pd.read_csv("../data/transacao_produto.csv", sep= ";")

dataf

#%%

filtro = (dataf["IdProduto"] == "5") | (dataf["IdProduto"] == "11")
dataf[filtro]

#%%


filtro = dataf["IdProduto"].isin(["5","11"])
dataf[filtro]

# %%

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes 

filtro = clientes["DtCriacao"].notna()
filtro

#%%

filtro = ~clientes["DtCriacao"].isna()
filtro


