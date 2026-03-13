#%%

import pandas as pd



df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()

#%%

max_pontos = df["qtdePontos"].max()
filtro = df["qtdePontos"] == max_pontos
df[filtro]

#%%
(df.sort_values(by="qtdePontos", ascending=False).
        head(5)["idCliente"])

#%%

brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "ana", "nah", "jose"],
        "idade": [32, 43, 35, 42],
        "salario":[2345, 4533, 3245, 4533],
    }
)
brinquedo

#%%

# Dois order by caso ouver empate

brinquedo.sort_values(by=["salario", "idade"], ascending=[False,True])

