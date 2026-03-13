#%%

import pandas as pd

#%%
df = pd.read_csv("../data/clientes.csv", sep=';')

idades = [32,44,12,54,67,32,23,34,32,12,45,43,28,73,29]

idades = pd.Series(idades)

df
#%%
idades.sum()
idades.describe()
# ...
#%%

redes_sociais = ["flEmail","flTwitch","flYouTube","flBlueSky","flInstagram"]

df[redes_sociais].mean()


#%%

