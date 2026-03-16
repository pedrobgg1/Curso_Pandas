#%%
import pandas as pd
import sqlalchemy as sql


#%%

engine = sql.create_engine("sqlite:///../data/olist.db")

#%%

clientes = pd.read_sql_table(table_name="tb_customers", 
                             con=engine)
#%%

query = "SELECT * " \
"FROM tb_customers " \
"WHERE customer_state = 'RS'" \
"" \

df_100 = pd.read_sql_query(query, con=engine)
df_100

#%%

