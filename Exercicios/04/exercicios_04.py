
#%%

import pandas as pd

df_clientes = pd.read_csv("../../data/clientes.csv", sep=";")
df_clientes

df_transacao = pd.read_csv("../../data/transacoes.csv", sep=";")
df_transacao
#%%

# Quantos clientes tem vínculo com a Twitch?

df_clientes.value_counts("flTwitch")[1]

#%%
# ou

filtro = df_clientes["flTwitch"] == 1
qtde_twitch  = df_clientes[filtro].shape[0]
qtde_twitch


#%%
# Quantos clientes tem um saldo de pontos maior que 1000?

filtro = df_clientes["qtdePontos"] > 1000
filtro
qtde_twitch  = df_clientes[filtro].shape[0]
qtde_twitch

#%%
# Quantas transações ocorreram no dia 2025-02-01?

df_transacao["data"] = pd.to_datetime(df_transacao["DtCriacao"]).dt.date
filtro = (df_transacao["DtCriacao"] >= "2025-02-01") & (df_transacao["DtCriacao"] < "2025-02-02")
qtde_transacao = df_transacao[filtro].shape[0]
qtde_transacao
