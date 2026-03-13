#%%
import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=';')
df.head()

#%%

# FUNCAO PARA SEPARAR O ULTIMO ELEMENTO DE UMA STRING

def get_last_id(x):
    return x.split("-")[-1]

#%%

# SEM USAR PANDAS


id_novo = []
for i in df["idCliente"]:
    id_novo.append(get_last_id(i))

id_novo
df["NovoId"] = id_novo
df.head()


#%%

# APLICAR FUNCAO ELEMENTO POR ELEMENTO

df["idCliente"].apply(get_last_id)


#%%

# Funções

def sep(x):
    return x.split(" ")

def get_day(x):
    x =  x[0]
    return x

def get_hour(x):
    x = x[1][:8]
    return x

# Applys


dias = df["DtCriacao"].apply(sep)

df["YMD"] = dias.apply(get_day)
df["HMS"] = dias.apply(get_hour)
df

#%%
