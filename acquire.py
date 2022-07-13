import pandas as pd
import numpy as np
import os
from env import host, user, password
# We import the required libraries and ensure the content from the env file is not actually displayed in this file.



def get_connection(db, user = user, host = host, password = password):
	return f'mysql+pymysql://{user}:{password}@{host}/{db}'
# This function will be used in other functions to connect with the required databases. 

def new_titanic_data():
	sql_query = 'SELECT * FROM passengers'
	df = pd.read_sql(sql_query, get_connection('titanic_db'))

	return df


def get_titanic_data():

	if os.path.isfile('titanic_df.csv'):
		df = pd.read_csv('titanic_df.csv', index_col = 0)
# if we already have a local file with the data, we can pull that
	else:
# otherwise we will pull from the db and create a .csv
		df = new_titanic_data()
		df.to_csv('titanic_df.csv')
	return df





def new_iris_data():
    sql_query = """
                SELECT 
                    species_id,
                    species_name,
                    sepal_length,
                    sepal_width,
                    petal_length,
                    petal_width
                FROM measurements
                JOIN species USING(species_id)
                """
    
    df = pd.read_sql(sql_query, get_connection('iris_db'))
    
    return df


def get_iris_data():
    if os.path.isfile('iris_df.csv'):
# if we already have a local file with the data, we can pull that        
        df = pd.read_csv('iris_df.csv', index_col=0)
        
    else:
# otherwise we will pull from the db and create a .csv        
        df = new_iris_data()
        
        df.to_csv('iris_df.csv')
        
    return df




def new_telco_data():
    sql_query = """
                select * from customers
                join contract_types using (contract_type_id)
                join internet_service_types using (internet_service_type_id)
                join payment_types using (payment_type_id)
                """
    
    df = pd.read_sql(sql_query, get_connection('telco_churn'))
    
    return df


def get_telco_data():
    if os.path.isfile('telco.csv'):
# if we already have a local file with the data, we can pull that           
        df = pd.read_csv('telco.csv', index_col=0)
        
    else:
# otherwise we will pull from the db and create a .csv        
        df = new_telco_data()
        
        df.to_csv('telco.csv')
        
    return df








