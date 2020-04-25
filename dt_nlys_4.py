import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from matplotlib.ticker import FormatStrFormatter as fsf


#os.chdir("/home/pranjal/Desktop/data_anlys/v2/std_1_4")
os.chdir(os.path.dirname(os.path.abspath(__file__))+'/v2/std_1_4')

def plottr_4(flnm):
    fls=sorted([fl for fl in os.listdir(".") if flnm in fl])
    print(fls)
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
    plt.ylabel('Vertical velocity (m/sec)') #based on quantity
    plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))    
    plt.legend(title="Speed (kmph)", loc='lower right')
    plt.tight_layout()
    plott.savefig('destination_path.eps', format='eps', dpi=1000)
    plt.show()

def arearead_4(flnm):
    fls=sorted([fl for fl in os.listdir(".") if flnm in fl])
    df = pd.read_csv(fls[0], sep="\s+",engine='python', header=0)
    ar_df = metrics.auc(df.iloc[:,0],abs(df.iloc[:,1]))
    df2 = pd.read_csv(fls[1], sep="\s+",engine='python', header=0)
    ar_df2 = metrics.auc(df2.iloc[:,0],abs(df2.iloc[:,1]))
    df3 = pd.read_csv(fls[2], sep="\s+",engine='python', header=0)
    ar_df3 = metrics.auc(df3.iloc[:,0],abs(df3.iloc[:,1]))
    df4 = pd.read_csv(fls[3], sep="\s+",engine='python', header=0)
    ar_df4 = metrics.auc(df4.iloc[:,0],abs(df4.iloc[:,1]))
    df5 = pd.read_csv(fls[4], sep="\s+",engine='python', header=0)
    ar_df5 = metrics.auc(df5.iloc[:,0],abs(df5.iloc[:,1]))
    #ar_all = [ar_df,ar_df2,ar_df3,ar_df4,ar_df5]
    ar_all = [ar_df2,ar_df3,ar_df4,ar_df5]
    return ar_all
    
def maxread_4(flnm):
    fls=sorted([fl for fl in os.listdir(".") if flnm in fl])
    df = pd.read_csv(fls[0], sep="\s+",engine='python', header=0)
    mx_df = max(abs(df.iloc[:,1]))
    df2 = pd.read_csv(fls[1], sep="\s+",engine='python', header=0)
    mx_df2 = max(abs(df2.iloc[:,1]))
    df3 = pd.read_csv(fls[2], sep="\s+",engine='python', header=0)
    mx_df3 = max(abs(df3.iloc[:,1]))
    df4 = pd.read_csv(fls[3], sep="\s+",engine='python', header=0)
    mx_df4 = max(abs(df4.iloc[:,1]))
    df5 = pd.read_csv(fls[4], sep="\s+",engine='python', header=0)
    mx_df5 = max(abs(df5.iloc[:,1]))
    #mx_all = [mx_df,mx_df2,mx_df3,mx_df4,mx_df5]
    mx_all = [mx_df2,mx_df3,mx_df4,mx_df5]
    return mx_all

def subPlotter_4(df,i,j):
    #plott = plt.figure()
    #plt.figure()
    a = ['BC-1','BC-2','BC-3']
    b = ['Ballast','Subballast','Subgrade']
    axs[i, j]
    axs[i, j].set_title(a[i]+', '+b[j])
    axs[i, j].set_xticks([100,200,400,600])
    #axs[i, j].set_ylim(0,0.4)
    #axs[i, j].set_yticks([0,0.1,0.2,0.3])
    axs[i, j].tick_params(direction="in",labelsize=8)
    axs[i, j].plot(df.iloc[:,0],df.iloc[:,1], marker='', markerfacecolor='blue', 
             markersize=2, color='black', linewidth=2, linestyle=':', label="Case 1")
    axs[i, j].plot(df.iloc[:,0],df.iloc[:,2], marker='', markerfacecolor='blue', 
             markersize=2, color='black', linewidth=2, linestyle='--', label="Case 2")
    axs[i, j].plot(df.iloc[:,0],df.iloc[:,3], marker='', markerfacecolor='blue', 
             markersize=2, color='black', linewidth=2, linestyle='-.', label="Case 3")
    axs[i, j].plot(df.iloc[:,0],df.iloc[:,4], marker='', markerfacecolor='black', 
             markersize=3, color='black', linewidth=1, linestyle='-', label="Case 4")
    axs[i,j].yaxis.set_major_formatter(fsf('%.2f'))

def all_cases(bc,lyr,quant):
    #a = sorted([fl for fl in os.listdir(".") if bc in fl if lyr in fl])
    fls = ['c1','c2','c3','c4']
    spd = [100,200,400,600]
    dt = []
    for i in fls:
        flnm = bc+i+'_'+lyr
        fls[len(dt)]=flnm
        dt.append(quant(flnm))
    fls.insert(0,'speed_'+str(quant).split(" ")[1])
    df = pd.DataFrame(list(zip(spd,dt[0],dt[1],dt[2],dt[3])), columns =fls)
    return df


a = ['bf_','ai_','af_']
b = ['blt_','sbt_','sbg_']

fig, axs = plt.subplots(nrows=3, ncols=3, sharex=True, sharey=True, figsize=(9, 6))
for i in range(len(a)):
    for j in range(len(b)):
        subPlotter_4(all_cases(a[i],b[j],maxread_4),i,j)

for ax in axs.flat:
    ax.set(xlabel='Speed (kmph)', ylabel='V2')
    ax.label_outer()

plt.legend(title="Load configuration", bbox_to_anchor=(0.78,-0.28),
           fontsize=10, ncol=4, bbox_transform=plt.gcf().transFigure)
plt.subplots_adjust(left=None, bottom=-0.2, right=None, top=None, wspace=None, hspace=None)
plt.show()  
fig.savefig('destination_path.eps', bbox_inches="tight",format='eps', dpi=1000)  
        