import pandas as pd 


def transf():
    
    url= "/usr/local/airflow/tests/Sales_data_dirty.csv"
    df=pd.read_csv(url)

    # Normalizar las variables de tipo categorica para limpiar la data 
    df['State'] = df['State'].str.lower().str.replace("^-", "").str.replace("-", " ").str.replace("  ", " ")
    df['Market'] = df['Market'].str.lower().str.replace("^-", "").str.replace("-", " ").str.replace("  ", " ") 
    df['Market Size'] = df['Market Size'].str.lower().str.replace("^-", "").str.replace("-", " ").str.replace("  ", " ")
    df['Date'] = df['Date'].str.lower().str.replace("^-", "").str.replace("-", " ").str.replace("  ", " ")
    df['Product Type'] = df['Product Type'].str.lower().str.replace("^-", "").str.replace("-", " ").str.replace("  ", " ")
    df['Product'] = df['Product'].str.lower().str.replace("^-", "").str.replace("-", " ").str.replace("  ", " ")
    df['Type'] = df['Type'].str.lower().str.replace("^-", "").str.replace("-", " ").str.replace("  ", " ")


    # Cambiar el nombre de las variables 
    df = df.rename(columns={"Budget Profit":"Budget_profit", "Area Code":"Area_code", "Budget Margin":"Budget_margin", "Budget Sales":"Budget_sales", "ProductId":"Product_ID"})
    df = df.rename(columns={"Total Expenses":"Total_expenses", "Budget COGS":"Budget_COGS", "Budget Margin":"Budget_margin", "Market Size":"Market_size","Product Type":"Product_type"})


    # Convertir las variables float a tipo int 
    df["Profit"]=df["Profit"].apply(int)
    df["Margin"]=df["Margin"].apply(int)
    df["Sales"]=df["Sales"].apply(int)
    df["COGS"]=df["COGS"].apply(int)
    df["Total_expenses"]=df["Total_expenses"].apply(int)
    df["Inventory"]=df["Inventory"].apply(int)
    df["Budget_profit"]=df["Budget_profit"].apply(int)
    df["Budget_COGS"]=df["Budget_COGS"].apply(int)
    df["Budget_margin"]=df["Budget_margin"].apply(int)
    df["Budget_sales"]=df["Budget_sales"].apply(int)
    df["Marketing"]=df["Marketing"].apply(int)




    # Convertir la variable Date de tipo object a tipo fecha 
    df['Date'] = df['Date'].apply(lambda row:row[0:8])
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%y')

    
    # Cambio de variables categoricas por variables enteras 
    df["Product_type"].replace(["coffee","tea", "espresso","herbal tea"], [0,1,2,3 ], inplace=True)
    df["Type"].replace(["regular","decaf"], [0,1 ], inplace=True)

    # Reemplazo de valores negativos por la medida de tendencia central median 
    df.loc[df['Profit'] <0, 'Profit'] = df.Profit.median()
    df.loc[df['Inventory'] <0, 'Inventory'] = df.Profit.median()


    #Guardar archivo en directorio test con datos limpios 
    df.to_csv("/usr/local/airflow/tests/Sales_data_clean.txt")
    df.to_csv("/usr/local/airflow/tests/Sales_data_clean.csv")