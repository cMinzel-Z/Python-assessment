# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:48:08 2019

@author: Minzel
"""
import pandas as pd
import matplotlib.pyplot as plt

def report(nobelprizeDict):
    import json
    with open(nobelprizeDict,"r") as f:
        info=f.read()
        d = json.loads(info)
    df_all=pd.DataFrame(d)
    year_cate = df_all.iloc[:,0:2]
    # if there were not laureates, it means not awarded.
    aw_or_n = df_all.iloc[:,2].notna()
    # I have checked columns 'year' and 'category'. There is no missing row.
    # conbine two tables with concat method is fine.
    df = pd.concat( [year_cate, aw_or_n], axis=1 )
    df = df.rename(columns={"laureates": "awarded_or_not"})
    # convert to correct types.
    df = df.astype({'year':'int','category':'str'})
    # for 'category' column, it shows it is obejct. 
    # So I check data type for each item in this column.
    print(df['category'].map(lambda x: type(x)))
    print(df.dtypes)
    return df
