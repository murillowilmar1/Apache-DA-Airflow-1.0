import pandas as pd 

# Algoritmos seleccionados 
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn import linear_model

# Metricas 
from sklearn.model_selection import train_test_split




def ML_model (): 

    url= "/usr/local/airflow/tests/Sales_data_clean.csv"
    df=pd.read_csv(url)
    # Almacenar Variables seleccionadoas para el algoritmo 
    Car_select =["Budget_margin","Budget_sales","Budget_COGS","Inventory","Total_expenses","Budget_profit", "Marketing"]
#Almacenar la variable objetivo 
    obj_select = df.Sales

# Almacenar datos en variables pequeñas para manipular datos en el modelo 
    X = df[Car_select]
    y = obj_select

    X_train, X_test, y_test, y_train = train_test_split(X, y, test_size = 0.20, random_state = 42)
    Reg_model = LinearRegression() 
    Reg_model.fit (X,y)

    Reg_model.score(X,y)