#%%

import pandas as pd

df = pd.read_csv("..\data\clientes.csv", sep=";")
df

#%%

df.to_csv("clientes.csv", index=False)

#%%
df.to_parquet("clientes.parquet", index=False)\

#%%
df.to_excel("clientes.xlsx", index=False)

#%%
df3 = pd.read_excel("clientes.xlsx")
df3


#%%

df_bobo = pd.read_csv("../data/bobo.csv",sep=";")
df_bobo