# -*- coding: utf-8 -*-
# import packages
import json 
import pandas as pd 
import numpy as np

#import TSV files from S3 location
f1 = 'https://upday-data-assignment.s3.eu-west-1.amazonaws.com/lake/2019-02-15.tsv'
f2 = 'https://upday-data-assignment.s3.eu-west-1.amazonaws.com/lake/2019-02-16.tsv'
f3 = 'https://upday-data-assignment.s3.eu-west-1.amazonaws.com/lake/2019-02-17.tsv'

# Convert to dataframes
t1 = pd.read_csv(f1, sep='\t', header=0)
t2 = pd.read_csv(f1, sep='\t', header=0)
t3 = pd.read_csv(f1, sep='\t', header=0)

#Apped all files into 1
T = t1.append(t2.append(t3)).reset_index()

#Create a copy for test
T_1 = T.copy()

# replace nan values
T_1['ATTRIBUTES'] = T_1['ATTRIBUTES'].fillna('{}')
T_1['ATTRIBUTES'] = T_1['ATTRIBUTES'].apply(json.loads)

# Flatten json and append columns to main DF
df_ATTRIBUTES = pd.json_normalize(T_1['ATTRIBUTES'])
complete_df = pd.concat([T_1, df_ATTRIBUTES], axis=1).drop('ATTRIBUTES', axis=1)


#prepare data for table article_performance 
stage = complete_df[['id', 'ID', 'TIMESTAMP', 'EVENT_NAME','title', 'category']][(complete_df.EVENT_NAME.str.contains("card")) | (complete_df.EVENT_NAME.str.contains("article"))].sort_values(by=['id']).reset_index(drop=True)

#limit the timestamp to only date part
stage['date'] = stage.TIMESTAMP.str[:10]


######### Prepare data for article_performance table #########
# count rows for events
art_perf = stage.groupby(['id', 'date','title', 'category', 'EVENT_NAME']
                ).size().unstack().reset_index().fillna(0)

# combine numbers for card view events
art_perf['card_views']=art_perf.my_news_card_viewed+art_perf.top_news_card_viewed

#create dataframe formatted for article_performance table
article_performance = art_perf.drop(['my_news_card_viewed', 'top_news_card_viewed'], axis=1).rename(columns={"article_viewed": "article_views", "id":"article_id"})

# reoder columns as per requirement
article_performance = article_performance[['article_id', 'date', 'title', 'category', 'card_views', 'article_views']]

######### ======================================================= #########
######### Prepare data for user_performance table #########
'''
The id column for user was not clear.
The "ID" column contained only 16 unique ids which accounted to few card views. 
They also did not have any article views. Due to this I continued using the "id" column instead to calculate the ctr.
'''

# prepare data for user performance table
usr_perf = article_performance[['article_id', 'date', 'card_views', 'article_views']]

# combine numbers for card view events
usr_perf['ctr']=usr_perf.article_views / usr_perf.card_views

#create dataframe formatted for user_performance table
user_performance  = usr_perf.drop(['article_views', 'card_views'], axis=1).rename(columns={"article_id": "user_id"}).reset_index(drop=True)
