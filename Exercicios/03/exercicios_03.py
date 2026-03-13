#%%
import pandas as pd

df_clientes = pd.read_csv("../../data/clientes.csv", sep=";")
df_clientes

#%%
#  Quantas linhas há no arquivo clientes.csv ?

df_clientes.shape[0]

#%%
# Quantas colunas do tipo int há no arquivo transacoes.csv ?

df_transacoes = pd.read_csv("../../data/transacoes.csv", sep=";")
df_transacoes
df_transacoes.dtypes

#%%
#  Quantas colunas do tipo object há no arquivo produtos.csv ?

df_produtos = pd.read_csv("../../data/produtos.csv", sep=";")
df_produtos
df_produtos.dtypes

#%%
# Qual o id do cliente no índice 4 no arquivo clientes.csv ?

df_clientes.iloc[4]["idCliente"]

#%%
# Qual o saldo de pontos do cliente na 10a posição (sem ordenar) do arquivo clientes.csv ?

df_clientes.iloc[9]["qtdePontos"]

