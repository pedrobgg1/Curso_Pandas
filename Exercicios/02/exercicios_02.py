#%%
import pandas as pd

df = pd.read_csv("../../data/transacoes.csv", sep=";")
df

#%%

df["coluna1"] = 1

#%%

df.to_csv("transacoes_1.csv", index=False)
