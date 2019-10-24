import pandas as pd
import matplotlib.pyplot as plt

def crosstab(var,df):
    '''
    generate table of no-show counts and proportions stratified by specified var
    '''
    b = pd.crosstab(index=df[var], columns=df['No_show'], margins=True)
    b['no_p'] = b['No']/b['All'] 
    b['yes_p'] = b['Yes']/b['All']
    return b

def bargraph(df):
    plt.figure(figsize=(15,6))
    plt.bar(df.index.values.astype(str),df['no_p']+df['yes_p'])
    plt.bar(df.index.values.astype(str),df['yes_p'])
    return plt.show();