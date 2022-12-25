from datetime import timedelta,datetime 
from dateutil.relativedelta import relativedelta
from airflow.utils.dates import days_ago 
from typing import Dict


from airflow import DAG
from airflow.operators.python import PythonOperator 
from airflow.providers.amazon.aws.transfers.local_to_s3 import LocalFilesystemToS3Operator
from airflow.operators.email import EmailOperator
from airflow.models.baseoperator import chain



from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn import linear_model

# Metricas 
from sklearn.model_selection import train_test_split


from dags.funtions.funtion_extr import extr_data
from dags.funtions.funtion_transf import transf
from dags.funtions.funtion_send_email import send_mail, send_mail2
from dags.funtions.funtion_ML_model import ML_model

import logging
import os 
#import pandas as pd 

# logger 
WORKING_DIR = os.getcwd()
LOGS_DIR = os.path.join(WORKING_DIR, 'tests')  
logger = logging.getLogger('Sales')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s', '%Y-%m-%d')
handler = logging.FileHandler(os.path.join(LOGS_DIR, 'Sales.log'))
handler.setFormatter(formatter)
logger.addHandler(handler)

default_args = {
    "owner": "wmurillo",
    "depends_on_past":False,
    "email": ["murillowilmar1@gmail.com"], 
    "email_on_failure": False,
    "email_on_retry": False,  
    "retries": 5, 
    "retry_delay":timedelta(minutes=1)
}




with DAG(

     "Sales_dag", 
     default_args=default_args,
     start_date= datetime(2022,1,12),
     max_active_runs =5, 
     description = " DAG_Sales",
     schedule_interval="@hourly", 
     tags=["DAG_Sales"], 
     catchup =False, 
     template_searchpath = "/usr/local/air_flow/include/"
) as dag: 

    
   
   
   #Task 1 
     extract_data= PythonOperator(task_id="extract_data", python_callable=extr_data)
   #Task 2 
     Transform_data = PythonOperator (task_id = "Transform_data", python_callable =transf)
   #Task 3 
     MACHL_model = PythonOperator (task_id = "ML_model", python_callable =ML_model)
   #Task 4 
     load_data_clean =LocalFilesystemToS3Operator(
        task_id = "load_data_clean",
        filename='/usr/local/airflow/tests/Sales_data_clean.csv',
        dest_key='Sales_data_clean.csv',
        dest_bucket='awswmurillo',
        aws_conn_id="aws_s3",
        replace=True
     )   
   #Task 5 
     load_MLmodel =LocalFilesystemToS3Operator(
        task_id = "load_data_ML",
        filename='/usr/local/airflow/tests/Reg_model.txt',
        dest_key='Reg_model.txt',
        dest_bucket='awswmurillo',
        aws_conn_id="aws_s3",
        replace=True
     )   
   #Task 6 
     Send_email_confirmation = PythonOperator (task_id = "Sen_email_confirmation", python_callable =send_mail2)    
   #Task 7 
     confirm_process =PythonOperator(task_id = "send_final_email", python_callable =send_mail)
            
      


     #chain(extract_data, Transform_data, [confirm_process, Ml_model], [weekday_activities, weekend_activities], end)
     
     chain(extract_data, Transform_data, [load_data_clean, MACHL_model],[Send_email_confirmation,load_MLmodel],confirm_process)
     #extract_data >> Transform_data>> confirm_process




