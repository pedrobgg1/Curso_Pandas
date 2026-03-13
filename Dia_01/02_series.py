#%%
idades = [ 
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 32,
]

media = sum(idades) / len(idades)

media

#%%

import pandas as pd

series_idade = pd.Series(idades)
series_idade

#%%

media = series_idade.mean()
variancia = series_idade.var()
print(media)
print(variancia)
summary = series_idade.describe()
print(summary)