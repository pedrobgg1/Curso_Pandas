#%%
import pandas as pd

df = pd.read_csv("dados_cartao.csv", sep=";")


df["dtTransacao"] = pd.to_datetime(df["dtTransacao"])

df["vlParcela"] = df["vlVenda"]/df["qtParcelas"]

df
#%%

df["OrdemParcela"] = df.apply(lambda row: [i for i in range(row["qtParcelas"])], axis=1)
df_explode = df.explode("OrdemParcela")
df_explode
#%%

def CalcDtParcela(row):
    dt = row["dtTransacao"] + pd.DateOffset(month=row["OrdemParcela"])
    dt = f"{dt.year}-{dt.month}"
    return dt

df_explode["dtParcela"] = (df_explode.apply(CalcDtParcela
                           ,axis=1)
)
df_explode
#%%

(df_explode.groupby(by=["idCliente","dtParcela"])
                   ["vlParcela"].sum()
                   .reset_index()

)
