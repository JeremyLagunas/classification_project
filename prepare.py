import pandas as pd
from pydataset import data
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import warnings
warnings.filterwarnings("ignore")
from env import host, user, password


import acquire
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
# We import the required libraries and ensure the content from the env file is not actually displayed in this file.



def prep_iris(df):
    cols_to_drop = ['species_id']
    # drop unnecessary column
    df = df.drop(columns = cols_to_drop)
    df.rename(columns = {'species_name':'species'}, inplace = True)
    df_dummy = pd.get_dummies(df['species'], dummy_na = False)
    df = pd.concat([df, df_dummy], axis = 1)
    return df


def prep_titanic(df):
    df = df.drop_duplicates()
    cols_to_drop = ['pclass', 'deck', 'embarked']
    df = df.drop(columns = cols_to_drop)
    dummy_df = pd.get_dummies(df[['sex', 'embark_town', 'class']], dummy_na = False, drop_first=[True, True])
    df = pd.concat([df, dummy_df], axis = 1)
    return df



def prep_telco(df):
    '''
    This function take in the df and returns a prepared version of the df by removing duplicates, removing unnecessary information, creating dummy columns and adding them to the df.
    '''
    df = df.drop_duplicates()
    # drop duplicates
    cols_to_drop = ['payment_type_id', 'internet_service_type_id', 'contract_type_id']
    df = df.drop(columns = cols_to_drop)
    # drop unnecessary columns
    dummy_df = pd.get_dummies(df[['contract_type', 'internet_service_type', 'payment_type']])
    # create dummy columns
    df = pd.concat([df, dummy_df], axis = 1)
    # concatenate the new columns to the old
    return df




def train_validate_test_split(df, target, seed=123):
    '''
    This function takes in a df, the target variable name (to stratify), and an integer for the seed.
    It then splits the data into train, validate and test. 
    Note: Only stratify if the target variable is categorical. If the target variable is continuous, then     remove stratification as an argument. 
    '''
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=seed, 
                                            stratify=df[target])
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=seed,
                                       stratify=train_validate[target])
    return train, validate, test


def split(df, stratify_by=None):
    """
    Crude train, validate, test split
    To stratify, send in a column name
    """
    
    if stratify_by == None:
        train, test = train_test_split(df, test_size=.2, random_state=123)
        train, validate = train_test_split(train, test_size=.3, random_state=123)
    else:
        train, test = train_test_split(df, test_size=.2, random_state=123, stratify=df[stratify_by])
        train, validate = train_test_split(train, test_size=.3, random_state=123, stratify=train[stratify_by])
    
    return train, validate, test
