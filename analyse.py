import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# ignore warning
pd.options.mode.chained_assignment = None  # default='warn'

df = pd.read_csv('live_project.csv')
df['difference'] =   df['Laurent Noel']-df['Live Project']
df_r0 = df[df['Cat'] == 'TRANSFORMATIONS-R+0']
df_r1 = df[df['Cat'] == 'TRANSFORMATIONS-R+1']
df_cuisine = df[df['chambre'] == 'cuisine_sam']
df_hall_burren = df[df['chambre'] == 'HALL ENTREE - BUREAU']
#sort by difference 
df.sort_values(by=['difference'], inplace=True, ascending=False)
df['sum_cum_live_project'] = df['Live Project'].cumsum()
df['sum_cum_Laurent_Noel'] = df['Laurent Noel'].cumsum()

# create df with R+0 in description 
df_r0['sum_cum_live_project'] = df_r0['Live Project'].cumsum()
df_r0['sum_cum_Laurent_Noel'] = df_r0['Laurent Noel'].cumsum()
df_r1['sum_cum_live_project'] = df_r1['Live Project'].cumsum()
df_r1['sum_cum_Laurent_Noel'] = df_r1['Laurent Noel'].cumsum()

def first_plot():
    sns.set()
    fig = plt.figure(figsize=(20,10)) 
    plt.plot(np.arange(len(df_r0)),df_r0['sum_cum_live_project'], label='Live Project R+0: '+str(int(df_r0['sum_cum_live_project'].iloc[-1]))+'€')
    plt.plot(np.arange(len(df_r0)),df_r0['sum_cum_Laurent_Noel'], label='Laurent Noel R+1: '+str(df_r0['sum_cum_Laurent_Noel'].iloc[-1])+'€')
    # plot df_r1
    plt.plot(np.arange(len(df_r1)),df_r1['sum_cum_live_project'], label='Live Project R+0: '+str(int(df_r1['sum_cum_live_project'].iloc[-1]))+'€')
    plt.plot(np.arange(len(df_r1)),df_r1['sum_cum_Laurent_Noel'], label='Laurent Noel R+1: '+str(df_r1['sum_cum_Laurent_Noel'].iloc[-1])+'€')
    #fill between
    plt.fill_between(np.arange(len(df_r0)), df_r0['sum_cum_live_project'], df_r0['sum_cum_Laurent_Noel'], color='blue', alpha=.1, label='diff = '+str(int(df_r0['sum_cum_Laurent_Noel'].iloc[-1]-df_r0['sum_cum_live_project'].iloc[-1]))+'€')
    plt.fill_between(np.arange(len(df_r1)), df_r1['sum_cum_live_project'], df_r1['sum_cum_Laurent_Noel'], color='orange', alpha=.1, label='diff = '+str(int(df_r1['sum_cum_Laurent_Noel'].iloc[-1]-df_r1['sum_cum_live_project'].iloc[-1]))+'€')

    plt.ylabel('Cumulative sum in €')
    plt.title('Cumulative sum of Live Project and Laurent Noel')
    plt.legend()
    plt.show()
def second_plot():
    #r+0 study 
    df_cuisine.sort_values(by=['difference'], inplace=True, ascending=False)
    df_cuisine['sum_cum_live_project'] = df_cuisine['Live Project'].cumsum()
    df_cuisine['sum_cum_Laurent_Noel'] = df_cuisine['Laurent Noel'].cumsum()

    fig = plt.figure(figsize=(20,10))
    plt.plot(np.arange(len(df_cuisine)),df_cuisine['sum_cum_live_project'], label='Live Project')
    plt.plot(np.arange(len(df_cuisine)),df_cuisine['sum_cum_Laurent_Noel'], label='Laurent Noel')
    # fiil between only in last index 
    plt.fill_between(np.arange(len(df_cuisine)), df_cuisine['sum_cum_live_project'], df_cuisine['sum_cum_Laurent_Noel'], where=(df_cuisine['sum_cum_live_project'] <= df_cuisine['sum_cum_Laurent_Noel']), color='red', alpha=0.1, interpolate=True,label= 'diff= '+str(int(df_cuisine['sum_cum_Laurent_Noel'].iloc[-1]-df_cuisine['sum_cum_live_project'].iloc[-1]))+'€')

    plt.ylabel('Cumulative sum in €')
    plt.title('Cumulative sum of Live Project and Laurent Noel: Cuisine SAM')

    plt.legend()
    plt.show()
    
def third_plot():
    #r+0 study 
    df_hall_burren.sort_values(by=['difference'], inplace=True, ascending=False)
    df_hall_burren['sum_cum_live_project'] = df_hall_burren['Live Project'].cumsum()
    df_hall_burren['sum_cum_Laurent_Noel'] = df_hall_burren['Laurent Noel'].cumsum()

    fig = plt.figure(figsize=(20,10))
    plt.plot(np.arange(len(df_hall_burren)),df_hall_burren['sum_cum_live_project'], label='Live Project')
    plt.plot(np.arange(len(df_hall_burren)),df_hall_burren['sum_cum_Laurent_Noel'], label='Laurent Noel')
    # fiil between only in last index 
    plt.fill_between(np.arange(len(df_hall_burren)), df_hall_burren['sum_cum_live_project'], df_hall_burren['sum_cum_Laurent_Noel'], where=(df_hall_burren['sum_cum_live_project'] <= df_hall_burren['sum_cum_Laurent_Noel']), color='red', alpha=0.1, interpolate=True,label= 'diff= '+str(int(df_hall_burren['sum_cum_Laurent_Noel'].iloc[-1]-df_hall_burren['sum_cum_live_project'].iloc[-1]))+'€')

    plt.ylabel('Cumulative sum in €')
    plt.title('Cumulative sum of Live Project and Laurent Noel: Hall Bureau')

    plt.legend()
    plt.show()