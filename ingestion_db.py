# First Python Script


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

from sqlalchemy import create_engine

import warnings
warnings.filterwarnings("ignore")



engine = create_engine('sqlite:///inventory.db')



def load_raw_data():

    # This Functions will load the CSVs as dataframe and ingest into db


    
    for file in os.listdir('data'):
      if'.csv'in file:
        df=pd.read_csv('data/'+file)
        print(df.shape)
        ingest_db(df,file[:-4],engine)


def ingest_db(df, table_name, engine):

    #This function will ingest the dataframe into database table

    
    df.to_sql(table_name,con = engine, if_exists = 'replace', index = False)