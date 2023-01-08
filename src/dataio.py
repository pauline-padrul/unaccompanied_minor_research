# -*- coding: utf-8 -*-
import sys
import time
import pandas as pd
import numpy as np
from pathlib import Path

# import streamlit as st
# from src.dictionaries import *
# from csv import writer
# from sqlalchemy import inspect, create_engine


# # Establish and define database connection
# connection_string = 'sqlite:///./data/Net_migration_rate_per1kpop_under18_Unicef.db'
# engine = create_engine(connection_string)
# insp = inspect(engine)

# Initialization data for demo and reproducable output
data_file = Path("../origin_data/Net_migration_rate_per1kpop_under18_Unicef_data.csv")


# def enumerate_df(data, col, dic):
#     data=data.replace({f"{col}": dic})
#     data.drop(data.loc[data[col]==0].index, inplace=True)
#     data.drop(data.loc[data[col]==''].index, inplace=True)
#     return data


def init_data():
    """
    Purpose:
        Initialize system data from local CSV files for reproducability
    Input:
        None
    Output (pd.DataFrame):
        Produces pandas DataFrames and corresponding SQL tables in SQLlite db file.
    
    """
    df = pd.read_csv(data_file, delimiter=",") #.rename(columns={"Unnamed: 0":"Ticker"})
    # df.to_sql('UMR', engine, index_label="Geo", index=False, if_exists='replace')
    # df.set_index("Geo", inplace=True)

    return df

def get_data(query):
    """
    Purpose:
        To return a dataframe to be used on the caller's page.
    Input (Str):
        Any SQL query string to perform on db
    Returns (pd.DataFrame):
        Pandas dataframe object

    """
    df = pd.read_sql_query(query, con=engine)
    return df