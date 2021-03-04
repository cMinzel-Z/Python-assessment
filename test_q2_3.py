# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 15:57:34 2019

@author: Minzel
"""
import pandas as pd
import matplotlib.pyplot as plt

def plot_freqs(nobelprizeDict):
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
    
    # get a part of table for question 2.3
    df_2_3 = df_al.drop(['year', 'laureate'], axis=1)
    # prepare tables for 6 plots
    df_che = df_2_3[df_2_3['category'].isin(['chemistry'])]
    df_eco = df_2_3[df_2_3['category'].isin(['economics'])]
    df_lit = df_2_3[df_2_3['category'].isin(['literature'])]
    df_pea = df_2_3[df_2_3['category'].isin(['peace'])]
    df_phy = df_2_3[df_2_3['category'].isin(['physics'])]
    df_med = df_2_3[df_2_3['category'].isin(['medicine'])]
    # prepare overallMotivation part
    df_o_che = df_che['overallMotivation'].dropna()
    df_o_eco = df_eco['overallMotivation'].dropna()
    df_o_lit = df_lit['overallMotivation'].dropna()
    df_o_pea = df_pea['overallMotivation'].dropna()
    df_o_phy = df_phy['overallMotivation'].dropna()
    df_o_med = df_med['overallMotivation'].dropna()
    
    # change motivation column to a list for word counting
    l_che = df_che.motivation.values.tolist()
    l_eco = df_eco.motivation.values.tolist()
    l_lit = df_lit.motivation.values.tolist()
    l_pea = df_pea.motivation.values.tolist()
    l_phy = df_phy.motivation.values.tolist()
    l_med = df_med.motivation.values.tolist()
    
    l_o_che = df_o_che.values.tolist()
    l_o_eco = df_o_eco.values.tolist()
    l_o_lit = df_o_lit.values.tolist()
    l_o_pea = df_o_pea.values.tolist()
    l_o_phy = df_o_phy.values.tolist()
    l_o_med = df_o_med.values.tolist()
    # change list to string for word counting
    str_che = " ".join(l_che)
    str_che = str_che.replace('"', '')
    str_eco = " ".join(l_eco)
    str_eco = str_eco.replace('"', '')
    str_lit = " ".join(l_lit)
    str_lit = str_lit.replace('"', '')
    str_pea = " ".join(l_pea)
    str_pea = str_pea.replace('"', '')   
    str_phy = " ".join(l_phy)
    str_phy = str_phy.replace('"', '')
    str_med = " ".join(l_med)
    str_med = str_med.replace('"', '')
    
    str_o_che = " ".join(l_o_che)
    str_o_che = str_o_che.replace('"', '')
    str_o_eco = " ".join(l_o_eco)
    str_o_eco = str_o_eco.replace('"', '')
    str_o_lit = " ".join(l_o_lit)
    str_o_lit = str_o_lit.replace('"', '')
    str_o_pea = " ".join(l_o_pea)
    str_o_pea = str_o_pea.replace('"', '')
    str_o_phy = " ".join(l_o_phy)
    str_o_phy = str_o_phy.replace('"', '')
    str_o_med = " ".join(l_o_med)
    str_o_med = str_o_med.replace('"', '')
    
    # convert txt file content into a list
    result = []
    with open('C:/Z_STUDY/Master/1_Python for Data Analysis/Coursework/whitelist.txt',"r") as f:
        for line in f:
            result.append(list(line.strip('\n').split(',')))
    result = [str(i) for i in result]
    # change it to string for extract words
    result_str = ",".join(result)
    # remove '' & []
    result_str = result_str.replace('[','').replace(']','').replace("\'","")
    # get a list of words for filter dict
    result = result_str.split(",")
    
    # word count fucntion
    def word_count(str):
        counts = dict()
        words = str.split()
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        return counts
    # apply to 6 dict
    dict_che = word_count(str_che)
    dict_eco = word_count(str_eco)
    dict_lit = word_count(str_lit)
    dict_pea = word_count(str_pea)
    dict_phy = word_count(str_phy)
    dict_med = word_count(str_med)
    
    dict_o_che = word_count(str_o_che)
    dict_o_eco = word_count(str_o_eco)
    dict_o_lit = word_count(str_o_lit)
    dict_o_pea = word_count(str_o_pea)
    dict_o_phy = word_count(str_o_phy)
    dict_o_med = word_count(str_o_med)
    # apply filter, keep words which included in txt file
    d_che = {k:v for k,v in dict_che.items() if k in result}
    d_eco = {k:v for k,v in dict_eco.items() if k in result}
    d_lit = {k:v for k,v in dict_lit.items() if k in result}
    d_pea = {k:v for k,v in dict_pea.items() if k in result}
    d_phy = {k:v for k,v in dict_phy.items() if k in result}
    d_med = {k:v for k,v in dict_med.items() if k in result}
    
    d_o_che = {k:v for k,v in dict_o_che.items() if k in result}
    d_o_eco = {k:v for k,v in dict_o_eco.items() if k in result}
    d_o_lit = {k:v for k,v in dict_o_lit.items() if k in result}
    d_o_pea = {k:v for k,v in dict_o_pea.items() if k in result}
    d_o_phy = {k:v for k,v in dict_o_phy.items() if k in result}
    d_o_med = {k:v for k,v in dict_o_med.items() if k in result}
    # merge dict
    def merge_dict(dica, dicb):
        dic = {}
        for key in dica:
            if dicb.get(key):
                dic[key]=dica[key]+dicb[key]
            else:
                dic[key]=dica[key]
        for key in dicb:
            if dica.get(key):
                pass
            else:
                dic[key]=dicb[key]
        return dic
    '''
    # get total counting for every word
    d_new = merge_dict(d_che,d_eco)
    d_new = merge_dict(d_new,d_lit)
    d_new = merge_dict(d_new,d_pea)
    d_new = merge_dict(d_new,d_phy)
    d_new = merge_dict(d_new,d_med)
  
    d_new = merge_dict(d_new,d_o_che)
    d_new = merge_dict(d_new,d_o_eco)
    d_new = merge_dict(d_new,d_o_lit)
    d_new = merge_dict(d_new,d_o_pea)
    d_new = merge_dict(d_new,d_o_phy)
    d_new = merge_dict(d_new,d_o_med)
    # total sequence for each word
    d_total = merge_dict(d_new,d_o_med)
    '''
    # sequence for each plot
    d_t_che = merge_dict(d_che, d_o_che)
    d_t_eco = merge_dict(d_eco, d_o_eco)
    d_t_lit = merge_dict(d_lit, d_o_lit)
    d_t_pea = merge_dict(d_pea, d_o_pea)
    d_t_phy = merge_dict(d_phy, d_o_phy)
    d_t_med = merge_dict(d_med, d_o_med)
    '''
    # change dict to dataframe for visualization
    df_t_p = pd.DataFrame.from_dict(d_total, orient='index', columns=['counts'])
    '''
    # df_che_p = pd.DataFrame.from_dict(d_t_che, orient='index', columns=['counts_che'])
    # df_eco_p = pd.DataFrame.from_dict(d_t_eco, orient='index', columns=['counts_eco'])
    # df_lit_p = pd.DataFrame.from_dict(d_t_lit, orient='index', columns=['counts_lit'])
    # df_pea_p = pd.DataFrame.from_dict(d_t_pea, orient='index', columns=['counts_pea'])
    # df_phy_p = pd.DataFrame.from_dict(d_t_phy, orient='index', columns=['counts_phy'])
    # df_med_p = pd.DataFrame.from_dict(d_t_med, orient='index', columns=['counts_med'])
    '''
    # combine them into one dataframe
    df_p = pd.concat([df_t_p, df_che_p, df_eco_p, df_lit_p, df_pea_p, df_phy_p, df_med_p],axis=1)
    '''
    
    # get correct oredered table for plot
    df_che_p_t = pd.DataFrame.from_dict(d_t_che, orient = 'index', columns=['counts'])
    df_che_p_t = df_che_p_t.reset_index().rename(columns = {'index': 'word'})
    df_che_p_t = df_che_p_t.sort_values(by="counts" , ascending=False)
    df_che_p_t['rank'] = range(1, len(df_che_p_t) + 1)
    
    df_eco_p_t = pd.DataFrame.from_dict(d_t_eco, orient = 'index', columns=['counts'])
    df_eco_p_t = df_eco_p_t.reset_index().rename(columns = {'index': 'word'})
    df_eco_p_t = df_eco_p_t.sort_values(by="counts" , ascending=False)
    df_eco_p_t['rank'] = range(1, len(df_eco_p_t) + 1)
    
    df_lit_p_t = pd.DataFrame.from_dict(d_t_lit, orient = 'index', columns=['counts'])
    df_lit_p_t = df_lit_p_t.reset_index().rename(columns = {'index': 'word'})
    df_lit_p_t = df_lit_p_t.sort_values(by="counts" , ascending=False)
    df_lit_p_t['rank'] = range(1, len(df_lit_p_t) + 1)
    
    df_pea_p_t = pd.DataFrame.from_dict(d_t_pea, orient = 'index', columns=['counts'])
    df_pea_p_t = df_pea_p_t.reset_index().rename(columns = {'index': 'word'})
    df_pea_p_t = df_pea_p_t.sort_values(by="counts" , ascending=False)
    df_pea_p_t['rank'] = range(1, len(df_pea_p_t) + 1)
    
    df_phy_p_t = pd.DataFrame.from_dict(d_t_phy, orient = 'index', columns=['counts'])
    df_phy_p_t = df_phy_p_t.reset_index().rename(columns = {'index': 'word'})
    df_phy_p_t = df_phy_p_t.sort_values(by="counts" , ascending=False)
    df_phy_p_t['rank'] = range(1, len(df_phy_p_t) + 1)
    
    df_med_p_t = pd.DataFrame.from_dict(d_t_med, orient = 'index', columns=['counts'])
    df_med_p_t = df_med_p_t.reset_index().rename(columns = {'index': 'word'})
    df_med_p_t = df_med_p_t.sort_values(by="counts" , ascending=False)
    df_med_p_t['rank'] = range(1, len(df_med_p_t) + 1)
    # get required 1st .. 50th word
    df_che_1 = df_che_p_t.loc[df_che_p_t['rank'] == 1,:]
    df_che_10 = df_che_p_t.loc[df_che_p_t['rank'] == 10,:]
    df_che_20 = df_che_p_t.loc[df_che_p_t['rank'] == 20,:]
    df_che_30 = df_che_p_t.loc[df_che_p_t['rank'] == 30,:]
    df_che_40 = df_che_p_t.loc[df_che_p_t['rank'] == 40,:]
    df_che_50 = df_che_p_t.loc[df_che_p_t['rank'] == 50,:]
    
    df_eco_1 = df_eco_p_t.loc[df_eco_p_t['rank'] == 1,:]
    df_eco_10 = df_eco_p_t.loc[df_eco_p_t['rank'] == 10,:]
    df_eco_20 = df_eco_p_t.loc[df_eco_p_t['rank'] == 20,:]
    df_eco_30 = df_eco_p_t.loc[df_eco_p_t['rank'] == 30,:]
    df_eco_40 = df_eco_p_t.loc[df_eco_p_t['rank'] == 40,:]
    df_eco_50 = df_eco_p_t.loc[df_eco_p_t['rank'] == 50,:]
    
    df_lit_1 = df_lit_p_t.loc[df_lit_p_t['rank'] == 1,:]
    df_lit_10 = df_lit_p_t.loc[df_lit_p_t['rank'] == 10,:]
    df_lit_20 = df_lit_p_t.loc[df_lit_p_t['rank'] == 20,:]
    df_lit_30 = df_lit_p_t.loc[df_lit_p_t['rank'] == 30,:]
    df_lit_40 = df_lit_p_t.loc[df_lit_p_t['rank'] == 40,:]
    df_lit_50 = df_lit_p_t.loc[df_lit_p_t['rank'] == 50,:]
    
    df_pea_1 = df_pea_p_t.loc[df_pea_p_t['rank'] == 1,:]
    df_pea_10 = df_pea_p_t.loc[df_pea_p_t['rank'] == 10,:]
    df_pea_20 = df_pea_p_t.loc[df_pea_p_t['rank'] == 20,:]
    df_pea_30 = df_pea_p_t.loc[df_pea_p_t['rank'] == 30,:]
    df_pea_40 = df_pea_p_t.loc[df_pea_p_t['rank'] == 40,:]
    df_pea_50 = df_pea_p_t.loc[df_pea_p_t['rank'] == 50,:]
    
    df_phy_1 = df_phy_p_t.loc[df_phy_p_t['rank'] == 1,:]
    df_phy_10 = df_phy_p_t.loc[df_phy_p_t['rank'] == 10,:]
    df_phy_20 = df_phy_p_t.loc[df_phy_p_t['rank'] == 20,:]
    df_phy_30 = df_phy_p_t.loc[df_phy_p_t['rank'] == 30,:]
    df_phy_40 = df_phy_p_t.loc[df_phy_p_t['rank'] == 40,:]
    df_phy_50 = df_phy_p_t.loc[df_phy_p_t['rank'] == 50,:]
    
    df_med_1 = df_med_p_t.loc[df_med_p_t['rank'] == 1,:]
    df_med_10 = df_med_p_t.loc[df_med_p_t['rank'] == 10,:]
    df_med_20 = df_med_p_t.loc[df_med_p_t['rank'] == 20,:]
    df_med_30 = df_med_p_t.loc[df_med_p_t['rank'] == 30,:]
    df_med_40 = df_med_p_t.loc[df_med_p_t['rank'] == 40,:]
    df_med_50 = df_med_p_t.loc[df_med_p_t['rank'] == 50,:]
    # combine into one table for make plot
    df_che_plot = pd.concat([df_che_1, df_che_10, df_che_20, df_che_30, df_che_40, df_che_50])
    df_eco_plot = pd.concat([df_eco_1, df_eco_10, df_eco_20, df_eco_30, df_eco_40, df_eco_50])
    df_lit_plot = pd.concat([df_lit_1, df_lit_10, df_lit_20, df_lit_30, df_lit_40, df_lit_50])
    df_pea_plot = pd.concat([df_pea_1, df_pea_10, df_pea_20, df_pea_30, df_pea_40, df_pea_50])
    df_phy_plot = pd.concat([df_phy_1, df_phy_10, df_phy_20, df_phy_30, df_phy_40, df_phy_50])
    df_med_plot = pd.concat([df_med_1, df_med_10, df_med_20, df_med_30, df_med_40, df_med_50])
    
    # get plot
    x = df_che_plot['rank']
    y = df_che_plot['counts']
    my_xticks = list(df_che_plot['word'].values)
    plt.scatter(x,y)
    plt.legend(['words counting'])
    plt.xticks(x, my_xticks)
    plt.title('chemistry')
    plt.ylabel('frequency')
    plt.show()
    
    x2 = df_eco_plot['rank']
    y2 = df_eco_plot['counts']
    my_xticks = list(df_eco_plot['word'].values)
    plt.scatter(x2,y2)
    plt.legend(['words counting'])
    plt.xticks(x2, my_xticks)
    plt.title('economics')
    plt.ylabel('frequency')
    plt.show()
    
    x3 = df_lit_plot['rank']
    y3 = df_lit_plot['counts']
    my_xticks = list(df_lit_plot['word'].values)
    plt.scatter(x3,y3)
    plt.legend(['words counting'])
    plt.xticks(x3, my_xticks)
    plt.title('literature')
    plt.ylabel('frequency')
    plt.show()
    
    x4 = df_pea_plot['rank']
    y4 = df_pea_plot['counts']
    my_xticks = list(df_pea_plot['word'].values)
    plt.scatter(x4,y4)
    plt.legend(['words counting'])
    plt.xticks(x4, my_xticks)
    plt.title('peace')
    plt.ylabel('frequency')
    plt.show()
    
    x5 = df_phy_plot['rank']
    y5 = df_phy_plot['counts']
    my_xticks = list(df_phy_plot['word'].values)
    plt.scatter(x5,y5)
    plt.legend(['words counting'])
    plt.xticks(x5, my_xticks)
    plt.title('physics')
    plt.ylabel('frequency')
    plt.show()
    
    x6 = df_med_plot['rank']
    y6 = df_med_plot['counts']
    my_xticks = list(df_med_plot['word'].values)
    plt.scatter(x6,y6)
    plt.legend(['words counting'])
    plt.xticks(x6, my_xticks)
    plt.title('medicine')
    plt.ylabel('frequency')
    plt.show()