#%%
import pandas as pd

df = pd.read_csv("../CasosPratica/DataFrame_Homicidios.csv", sep=";")

#%%

df_stack = (df.set_index(["nome","período"])
        .stack()
        .reset_index()
        .rename(columns={'level_2':'TipoHomicidio', 0:'QtHomicidio'})
)
df_stack

#%%

df_unstack = (df_stack.set_index(["nome","período","TipoHomicidio"])
            .unstack()
            .reset_index())
#%%

metricas = df_unstack.columns.droplevel(0)[2:].tolist()
df_unstack.columns = ['nome','período'] + metricas
df_unstack