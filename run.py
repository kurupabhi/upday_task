#import pandas as pd
import psycopg2
import sqlalchemy
from upday_etl import article_performance, user_performance
from time import sleep

sleep(10)

## Assign dataframes to local variables
art_perf = article_performance
usr_perf = user_performance

## Set connection parameters
user='user',
password='password',
host='postgres',
database='database'
engine = sqlalchemy.create_engine('postgresql+psycopg2://{0}:{1}@{2}/{3}'.
                                               format(user, password, 
                                                      host, database), pool_recycle=3600)

## Insert dataframe to Postgres tables
try:
    art_perf.to_sql(con=engine, name='article_performance', if_exists='replace',index=False)
    usr_perf.to_sql(con=engine, name='user_performance', if_exists='replace',index=False)
except (Exception, psycopg2.Error) as error:
    print('Error while connecting to PostgreSQL', error)
