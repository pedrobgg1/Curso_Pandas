#%%
import pandas as pd

import numpy as np

#%%
df = pd.read_csv("../data/transacoes.csv", sep=';')
df.head()

#%%

def conta(x: pd.Series):
    amplitude = x.max() - x.min()
    media = x.mean()
    return np.sqrt((amplitude - media)**2)


def life_time(x: pd.Series):
        dt = pd.to_datetime(x)
        diff = (dt.max() - dt.min()).days
        return diff

idades = pd.Series([21,32,43,32,14,65,78,34,19])
conta(idades)

#%%

summary =(df.groupby(by=["IdCliente"], as_index=False)
                        .agg({"IdTransacao":['count'],
                              "QtdePontos":['sum','mean',conta],
                              "DtCriacao":[life_time]
                              })
)

summary.columns = [
    "idCliente",
    "qtdeTransacao",
    "totalPontos",
    "mediaPontos",
    "ampMeanDiff",
    "lifeTime",
]

summary