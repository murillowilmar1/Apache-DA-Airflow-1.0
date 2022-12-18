import pandas as pd 
from urllib import request


url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ2dd5cqitVNVExzhZUiz-LbSJd4goEOzzaOCPGQJfIkrN_k_3fm38ePFQR-TM-xoTzRPypI4jr10FD/pub?gid=1687017788&single=true&output=csv"
local_file = "C:/Users/Usuario/OneDrive/Escritorio/Apache_Airflow_Project 1.0/Sales_Data/sales.csv"
request.urlretrieve(url, local_file)


# pandas para verificar  datos 
url2="C:/Users/Usuario/OneDrive/Escritorio/Apache_Airflow_Project 1.0/Sales_Data/sales.csv"
sales = pd.read_csv(url2)
print(sales)




