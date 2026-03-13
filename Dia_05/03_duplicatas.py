#%%

import pandas as pd

df = pd.DataFrame({
    "nome": ['teo', 'lara', 'nah', 'bia', 'mah', 'lara', 'mah', 'mah'],
    "sobrenome": ['calvo', 'calvo', 'ataide', 'ataide', 'silva', 'silva', 'silva', 'silva'],
    "salario": [2132, 1231, 454, 6543, 6532, 4322, 987, 2134],
})
df
#%%
# mantem a primeira e dropa as outras duplicatas

df.drop_duplicates()


#%%

df.drop_duplicates(keep="last")

#%%

# dropas quando colunas especificas sao iguais
# pode usar o sort.value para indicar qual quer deixar como o maior salario

df = df.sort_values("salario", ascending=False)
df.drop_duplicates(subset=["nome","sobrenome"])

#%%

# deixar mais clean 

df = (df.sort_values("salario", ascending=False)
    .drop_duplicates(subset=["nome","sobrenome"]))
df
