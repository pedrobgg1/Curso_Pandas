#%% 

import pandas as pd

transacao_produto = pd.read_csv("../../data/transacao_produto.csv", sep=";")

produto = pd.read_csv("../../data/produtos.csv", sep=";")

cliente = pd.read_csv("../../data/clientes.csv", sep=";")

transacoes = pd.read_csv("../../data/transacoes.csv", sep=";")


#%%
# Quem teve mais transações de Streak?

transacao_produto

#%%
transacoes

#%%

join_transcoes = transacoes.merge(
    right=transacao_produto,
    how='left',
    on="IdTransacao"
)

double_join = join_transcoes.merge(
    right=produto,
    how="left",
    on="IdProduto"
)

df_full = double_join[double_join["IdProduto"] == "11"]

df_full.groupby(by=["IdCliente"]).agg({"IdTransacao":['count']})

#%%

# UMA FORMA MAIS LEVE DE RODAR O CODIGO

produto2 = produto[produto["DescNomeProduto"] =="Lista de presença"]

join_transcoes = (transacoes
    .merge(right=transacao_produto,how='left',on="IdTransacao")
    .merge(produto2,on="IdProduto", how='right')
    .groupby(by="IdCliente")["IdTransacao"]
    .count()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)
join_transcoes

