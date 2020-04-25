import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from matplotlib.ticker import FormatStrFormatter as fsf

def read_8(flnm,quant):
    fls=sorted([fl for fl in os.listdir(".") if flnm in fl])
    df_list = []
    c = pd.DataFrame()
    for i in fls:
        c = pd.read_csv(i, sep="\s+",engine='python', header=0)
        if(quant=='area'):
            df_list.append(metrics.auc(c.iloc[:,0],abs(c.iloc[:,1])))
        elif(quant=='ptp'):
            df_list.append(max(c.iloc[:,1])-min(c.iloc[:,1]))
        else:
            df_list.append(max(abs(c.iloc[:,1])))       
    return df_list

def subPlotter_8(df,i,axs): 
    a = ['Ballast','Subballast','Subgrade'] #['Study-1','Study-2','Study-3','Study-4']
    axs[i]
    axs[i].set_title(a[i])
    axs[i].set_xticks([0,25,50,75,100,125,150,175,200])
    axs[i].tick_params(direction="in",labelsize=8)
    axs[i].plot(df.iloc[:,0],df.iloc[:,1], marker='', markerfacecolor='blue', 
             markersize=2, color='black', linewidth=2, linestyle=':', label="Study-1")
    axs[i].plot(df.iloc[:,0],df.iloc[:,2], marker='', markerfacecolor='blue', 
             markersize=2, color='black', linewidth=2, linestyle='--', label="Study-2")
    axs[i].plot(df.iloc[:,0],df.iloc[:,3], marker='', markerfacecolor='blue', 
            markersize=2, color='black', linewidth=2, linestyle='-.', label="Study-3")
    axs[i].plot(df.iloc[:,0],df.iloc[:,3], marker='', markerfacecolor='black', 
             markersize=3, color='black', linewidth=1, linestyle='-', label="Study-4")
    axs[i].yaxis.set_major_formatter(fsf('%.2f'))
    #axs[i].locator_params(axis='y', nbins=5)

def subPlotter_8_1(df,i,axs): 
    a = ['Study-1','Study-2','Study-3','Study-4'] # ['Ballast','Subballast','Subgrade']
    axs[i]
    axs[i].set_title(a[i])
    axs[i].set_xticks([0,25,50,75,100,125,150,175,200])
    axs[i].tick_params(direction="in",labelsize=8)
    axs[i].plot(df.iloc[:,0],df.iloc[:,1], marker='', markerfacecolor='blue', 
             markersize=2, color='black', linewidth=2, linestyle='-.', label="Ballast")
    axs[i].plot(df.iloc[:,0],df.iloc[:,2], marker='', markerfacecolor='blue', 
             markersize=2, color='black', linewidth=2, linestyle='--', label="Subballast")
    axs[i].plot(df.iloc[:,0],df.iloc[:,3], marker='', markerfacecolor='black', 
             markersize=3, color='black', linewidth=1, linestyle='-', label="Subgrade")
    axs[i].yaxis.set_major_formatter(fsf('%.2f'))
    axs[i].locator_params(axis='y', nbins=5)
