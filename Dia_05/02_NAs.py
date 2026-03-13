#%%

import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")
df

#%%

df.dropna()

#%%

df = pd.DataFrame(
    {
        "nome": ["Téo", None, "Nah", "Marcio"],
        "idade": [None, None, 43, 52],
        "salario": [3453,4324,None,5423]
    }
)

#%%

# dropar na apenas de uma coluna

df.dropna(how="all", subset=["idade"])


#%%

# se usar all + 2 colunas ele vai dropar apenas quando tiver nulo nas duas ao mesmo tempo

df.dropna(how="all", subset=["idade","salario"])

#%%
# any ja dropa se tiver em uma linha anyway 
df.dropna(how="any", subset=["idade","salario"])


#%%

# FILL NA

df["idade"] = df["idade"].fillna(0)
df

#%%

df = df.fillna({"nome":"ninguem", "idade":12})
df

#%%

medias = df[["idade","salario"]].mean()
df.fillna(medias)