#%%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df


#%%

df.shape

#%%

df.info(memory_usage='deep')

#%%
df.dtypes

#%%

# Renomear colunas    
# criar dicionario com a chave sendo o nome antigo e o valor o nome novo
df = df.rename( columns={"QtdePontos":"qtpontos", 
                         "DescSistemaOrigem":"SistemaOrigem"})

#%%
renamed_columns = {
    "QtdePontos":"qtpontos", 
    "DescSistemaOrigem":"SistemaOrigem"
}

# inplace = true
# nao precisa colocar df = 
df.rename(columns=renamed_columns, inplace=True)

#%%
colunas = ["IdCliente", "qtpontos"]

df[colunas]

#%%

#select * from df

df

#%%
#select idcliente from df

df[["IdCliente"]]

#%%

#select idcliente, qtpontos from df limit 5


df[["IdCliente", "qtpontos"]].sample(5)


#%%

# select idcliente, idtransacao, qtpontos
# from df
#limit 5

df[["IdCliente", "qtpontos", "IdTransacao"]].sample(5)

#%%


colunas = list(df.columns)
colunas.sort()
colunas


df = df[colunas]
df

