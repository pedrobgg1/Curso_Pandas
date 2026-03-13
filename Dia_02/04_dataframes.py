#%%
import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")
df_clientes
# %%

# Primeiros
df_clientes.head(n=10)

#%%

# Ultimos
df_clientes.tail(n=10)

#%%

# Aleatorios
df_clientes.sample(10)

#%%
df_clientes.shape

#%%
df_clientes.columns

#%%
df_clientes.index

#%%

df_clientes.info(memory_usage='deep', max_cols=2)


#%%

df_clientes.dtypes["flEmail"]

