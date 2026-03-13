#%%

import pandas as pd


df = pd.read_csv("../data/clientes.csv", sep=";")

df

#%%

df["qtdePontos"].astype(float)

#%%

pd.to_datetime(df["DtCriacao"])

#%%
# corrigindo linhas invalidas com o .replace

df["DtCriacao"] = df["DtCriacao"].replace({
    "2025-10-29 02:08:18.367": "2024-02-01 00:00:00.000"
})

pd.to_datetime(df["DtCriacao"])


# OU 

#%%

replace = {"2025-10-29 02:08:18.367": "2024-02-01 00:00:00.000"}

df["DtCriacao"] = pd.to_datetime(df["DtCriacao"].replace(replace))
print(df["DtCriacao"])

#%%

# Converter para data libera o uso do dt. (informacao que quer pegar ex: day, year, month etc)

df["DtCriacao"].dt.month_name()

