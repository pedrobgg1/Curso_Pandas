#%%

import pandas as pd

idades = [ 
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39,
]

series_idade = pd.Series(idades)
series_idade

#%%
print(idades[0])
print(idades[-1])

print(series_idade[0])

tamanho = len(series_idade) -1

print(series_idade[tamanho])

#%%

series_idade = series_idade.sort_values()
series_idade

#%%

# O indice é vinculado ao numero na origem mesmo se reordenar

series_idade[0]

#%%

# ILOC: Pega a posicao dependendo do ordenamento

print(series_idade.iloc[0])

print(series_idade.iloc[-1])

print(series_idade.iloc[:3])

print(series_idade.iloc[:: -2])

#%

idades = [ 
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39,
]


indexs = [
    "Téo", "Maria", "Jose", "Luis", "Ana",
    "Nah", "Dani", "Mah", "Fer", "Nanda",
    "Naty", "Nih", "Pedro", "Kozato", "Kozato",
]

series_idades = pd.Series(idades, index=indexs)
series_idades

#%%

print(series_idades["Kozato"])
print(series_idades.iloc[-1])