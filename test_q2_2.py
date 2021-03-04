# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 14:28:45 2019

@author: Minzel
"""

import pandas as pd

def get_laureates_and_motivation(nobelprizeDict, year, category):
    # your code here
    import json
    with open(nobelprizeDict,"r") as f:
        info=f.read()
        d = json.loads(info)
    # get whole table
    df_all=pd.DataFrame(d)
    df_all = df_all.astype({'year':'int','category':'str'})
    # create unique id for each row
    df_all['new_col'] = range(1, len(df_all) + 1)
    # extract laureates into multiple rows
    s = df_all.apply(lambda x: pd.Series(x['laureates']), axis=1).stack().reset_index(level=1, drop=True)
    s.name = 'laureate'
    df2 = df_all.drop('laureates', axis=1).join(s)
    df2['laureate'] = pd.Series(df2['laureate'], dtype=object)
    # delete row which has no laireate 
    df3 = df2.dropna(subset=['laureate'])
    # extract each item for every laureate
    df4 = df3['laureate'].apply(pd.Series)
    # make sure every laureate name could display not NaN
    df4['firstname'] = df4['firstname'].fillna(value=' ')
    df4['surname'] = df4['surname'].fillna(value=' ')
    # combine laureate's name into one column
    df5 = df4['firstname'].str.cat(df4['surname'], sep = ' ')
    # redesign the structure of tables to get the correct order and structure which is required by assessment
    df4 = df4.drop(['share', 'firstname', 'surname'], axis=1)
    df4 = pd.concat([df4['id'], df5, df4['motivation']], axis=1)
    df4 = df4.rename(columns={'firstname':'laureate'})
    df_al = pd.concat([df3['category'], df3['year'], df4, df3['overallMotivation']], axis=1)
    # change data types for each column
    df_al = df_al.astype({'year':'int','category':'str', 'id':'int', 'laureate':'str', 'motivation':'str'})
    # use required two parameters to qurey
    df = df_al[df_al['year'].isin([year]) & df_al['category'].isin([category])]
    return df