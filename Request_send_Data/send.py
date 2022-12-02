
#Libreria para enviar tabla a base de datos en Postgresql
from sqlalchemy import create_engine

#Importar tabla de archivo Request.py 
from Request import sales

# Utilizar variable para conexión 

engine = create_engine ("postgresql://postgres:2369115@localhost:5432/challenge")

# Pasar tabla  a SQL 
sales.to_sql("sales_data", con=engine, if_exists="replace")
