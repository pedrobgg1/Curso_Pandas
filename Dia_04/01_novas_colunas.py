#%%

import pandas as pd
import numpy as np


df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()

#%%

df["pontos_100"] = df["qtdePontos"] + 100
df.head()


#%%

df["EeT"] = df["flEmail"] + df["flTwitch"]
df

#%%

df["EoT"] = df["flEmail"] * df["flTwitch"]
df

#%%

df["EeT"] = df["flEmail"] + df["flTwitch"]

df["QtRedes"] = df["flEmail"]+df["flTwitch"]+df["flYouTube"]+df["flBlueSky"]+df["flInstagram"]
df
# %%

df["qtdePontos"].describe()

#%%

df["logpontos"] = np.log(df["qtdePontos"]+1)
df["logpontos"].describe()


