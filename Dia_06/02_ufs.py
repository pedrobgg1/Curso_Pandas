# %%

import pandas as pd
import io
import requests as rqs

#%%
url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = rqs.get(url, headers=headers)

df_list = pd.read_html(io.StringIO(response.text))
uf = df_list[1]
uf
# %%
def str_to_float(x:str):
    x = (x.replace(" ", "")
          .replace(",", ".")
          .replace("\xa0", "")
            )
    return float(x)

#%%

uf.dtypes
#%%
colunas = ["Área (km²)","População (Censo 2022)", "PIB (2015)", "PIB per capita (R$) (2015)"]

for i in colunas:
    uf[i] = uf[i].apply(str_to_float)
uf.dtypes

#%%

def exp(x):
    return float(x.replace(",",".")
                .replace(" anos",""))
  
uf["Expectativa de vida (2016)"] = uf["Expectativa de vida (2016)"].apply(exp)

#%%
uf.dtypes

#%%

coluna = "Alfabetização (2016)"

def alf_to_float(x:str):
    x = x.replace("%","").replace(",",".")
    x = float(x)
    x = x/100
    return x

uf[coluna] = uf[coluna].apply(alf_to_float)

#%%
uf.rename(columns=({coluna:"% De Alfabetização (2016)"}),inplace=True)
uf


#%%
coluna3 = "Mortalidade infantil (2016)"

def mort_to_float(x:str):
    x = float(x.replace("‰","").replace(",","."))
    return x

uf[coluna3] = uf[coluna3].apply(mort_to_float)
#%%
uf.rename(columns=({coluna3:"Mortalidade infantil /1000 (2016)"}),inplace=True)
uf

#%%

def uf_to_regiao(uf):

    if uf in ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"]:
        return "Centro-Oeste"
    elif uf in ["Alagoas","Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"]:
        return "Nordeste"
    elif uf in ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"]:
       return "Norte"
    elif uf in ["Espírito Santo","Minas Gerais", "Rio de Janeiro", "São Paulo"]:
        return "Sudeste"
    elif uf in ["Paraná", "Rio Grande do Sul", "Santa Catarina"]:
        return "Sul"
    
uf["Região"] = uf["Unidade federativa"].apply(uf_to_regiao)
uf

#%%

def classifica_bom(linha):
    return (linha["PIB per capita (R$) (2015)"] > 30000 and
            linha["Mortalidade infantil /1000 (2016)"] < 15 and 
            linha["IDH (2010)"] > 700)

# %%

uf.apply(classifica_bom, axis=1)

# %%

uf.apply(lambda x: x["PIB per capita (R$) (2015)"], axis=1)
