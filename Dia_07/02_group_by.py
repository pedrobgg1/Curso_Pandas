#%%
import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=';')
df.head()

#%%

df.groupby(by=["IdCliente"], as_index=False)[["IdTransacao"]].count()

#%%

summary = (df.groupby(by=["IdCliente"], as_index=False)
                    .agg({"IdTransacao": ['count'],
                          "QtdePontos":['sum', 'mean']})
                    
)
summary



#%%

summary.columns = ["IdCliente","qtdtransacao","totalpontos","avggpontos"]
summary

#%%

