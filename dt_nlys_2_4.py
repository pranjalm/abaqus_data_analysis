import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from matplotlib.ticker import FormatStrFormatter as fsf

#os.chdir("/home/pranjal/Desktop/data_anlys/v2/std_2_8")
os.chdir(os.path.dirname(os.path.abspath(__file__))+'/s22/std_2_4')


def plottr_4(flnm):
    fls=sorted([fl for fl in os.listdir(".") if flnm in fl])
    df = pd.read_csv(fls[0], sep="\s+",engine='python', header=0)
    df2 = pd.read_csv(fls[1], sep="\s+",engine='python', header=0)
    df3 = pd.read_csv(fls[2], sep="\s+",engine='python', header=0)
    df4 = pd.read_csv(fls[3], sep="\s+",engine='python', header=0)
    df5 = pd.read_csv(fls[4], sep="\s+",engine='python', header=0)
    plott = plt.figure()
    plt.plot(df.iloc[:,0],df.iloc[:,1], marker='', markerfacecolor='blue', 
             markersize=2, color='black', linewidth=2, linestyle=':', label="0")
    plt.plot(df2.iloc[:,0],df2.iloc[:,1], marker='', markerfacecolor='blue', 
             markersize=2, color='black', linewidth=2, linestyle='--', label="100")
    plt.plot(df3.iloc[:,0],df3.iloc[:,1], marker='', markerfacecolor='blue', 
             markersize=2, color='black', linewidth=2, linestyle='-.', label="200")
    plt.plot(df4.iloc[:,0],df4.iloc[:,1], marker='.', markerfacecolor='black', 
             markersize=3, color='black', linewidth=1, linestyle='--', label="400")
    plt.plot(df5.iloc[:,0],df5.iloc[:,1], marker='', markerfacecolor='blue', 
             markersize=2, color='black', linewidth=2, linestyle='-.', label="600")
    
    plt.xlim(0,300)
    plt.xlabel('Distance along the path (m)')
    if(df.iloc[:,1].max()>200):
        plt.ylabel('Vertical stress (Pa)')
    else:
        plt.ylabel('Vertical velocity (m/sec)')
    plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))    
    plt.legend(title="Speed (kmph)", loc='lower right')
    plt.tight_layout()
    plott.savefig('destination_path.eps', format='eps', dpi=1000)
    plt.show()
#plottr_4('ic_blt')
def read_4(flnm,quant):
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
    #print(fls)
    return df_list
read_4('ic_blt','area')
def subPlotter_4(df,i): 
    #a = ['Study-1','Study-2','Study-3','Study-4']
    a = ['Ballast','Subballast','Subgrade']
    axs[i]
    axs[i].set_title(a[i])
    axs[i].set_xticks([100,200,400,600])
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
#plottr_4('ic_blt')

def all_cases(lyr,quant):
    fls = ['ic','ie','xc','xe'] #['Study-1','Study-2','Study-3','Study-4']
    spd = [0,100,200,400,600]
    dt = []
    for i in fls:
        flnm = i+'_'+lyr
        fls[len(dt)]=flnm
        dt.append(read_4(flnm,quant))
    fls.insert(0,'speed_'+quant)
    #df = pd.DataFrame(list(zip(spd,dt[0],dt[1],dt[2],dt[3])), columns =fls)
    df = pd.DataFrame(list(zip(spd,dt[0],dt[1],dt[2],dt[3])), columns =fls)
    return df

#print(all_cases('blt_',ptpread_4))

b = ['blt_','sbt_','sbg_']
fig, axs = plt.subplots(nrows=3, ncols=1)#, sharex=True, sharey=True, figsize=(9, 6))
for j in range(len(b)):
    subPlotter_4(all_cases(b[j],'area'),j)

for ax in axs.flat:
    ax.set(xlabel='Speed (kmph)', ylabel='V2')
    ax.label_outer()

plt.legend(title="Load configuration", bbox_to_anchor=(0.9,-0.3),
           fontsize=10, ncol=4, bbox_transform=plt.gcf().transFigure)
plt.subplots_adjust(left=None, bottom=-0.2, right=None, top=None, wspace=None, hspace=None)
plt.show()  
fig.savefig('destination_path.eps', bbox_inches="tight",format='eps', dpi=1000) 