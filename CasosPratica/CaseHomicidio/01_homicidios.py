#%%
import pandas as pd
import os


#%%
def read(file_name):
    df = (pd.read_csv(f"../data/ipea/as/{file_name}.csv", sep=";")
            .rename(columns={"valor":file_name})
            .set_index(["nome", "período"])
            .drop(["cod"],axis=1)
            )
    
    return df

#%%
file_names = os.listdir("../data/ipea/as/")

dfs=[]

for i in file_names:
    dfs.append(read(i.split(".")[0]))

#%%

df_geral = pd.concat(dfs , axis=1).reset_index().sort_values(["período","nome"], ascending=False)
df_geral.to_csv("DataFrame_Homicidios.csv", index=False, sep=";")
