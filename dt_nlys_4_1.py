import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from matplotlib.ticker import FormatStrFormatter as fsf

os.chdir(os.path.dirname(os.path.abspath(__file__))+'/u2/std_1_4')

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
    return df_list
print(read_4('af_c1_blt','area'))
def subPlotter_4(df,i,j):
    #plott = plt.figure()
    #plt.figure()
    a = ['BC-1','BC-2','BC-3']
    b = ['Case-1','Case-2','Case-3','Case-4']
    axs[i, j]
    axs[i, j].set_title(a[i]+', '+b[j])
    axs[i, j].set_xticks([0,100,200,400,600])
    #axs[i, j].set_ylim(0,0.4)
    #axs[i, j].set_yticks([0,0.1,0.2,0.3])
    axs[i, j].tick_params(direction="in",labelsize=8)
    axs[i, j].plot(df.iloc[:,0],df.iloc[:,1], marker='', markerfacecolor='blue', 
             markersize=2, color='black', linewidth=2, linestyle=':', label="Ballast")
    axs[i, j].plot(df.iloc[:,0],df.iloc[:,2], marker='', markerfacecolor='blue', 
             markersize=2, color='black', linewidth=2, linestyle='--', label="Subballast")
    axs[i, j].plot(df.iloc[:,0],df.iloc[:,3], marker='', markerfacecolor='blue', 
             markersize=2, color='black', linewidth=2, linestyle='-.', label="Subgrade")
    axs[i,j].yaxis.set_major_formatter(fsf('%.2f'))

def all_cases(cs,lyr,quant):
    #a = sorted([fl for fl in os.listdir(".") if cs in fl if lyr in fl])
    fls = ['blt_','sbt_','sbg_']
    spd = [0,100,200,400,600]
    dt = []
    for i in fls:
        flnm = lyr+cs+'_'+i
        fls[len(dt)]=flnm
        dt.append(read_4(flnm,quant))
    fls.insert(0,'speed_'+quant)
    df = pd.DataFrame(list(zip(spd,dt[0],dt[1],dt[2])), columns =fls)
    return df

a = ['ai_','bf_','af_']
b = ['c1','c2','c3','c4']
 # ai = bc-1 infinite, bf = bc-2 bottom_finite , af = bc-3 finite
#b = ['blt_','sbt_','sbg_']

fig, axs = plt.subplots(nrows=3, ncols=4, sharex=True, sharey=True, figsize=(9, 6))
for i in range(len(a)):
    for j in range(len(b)):
        subPlotter_4(all_cases(b[j],a[i],'area'),i,j)

for ax in axs.flat:
    ax.set(xlabel='Speed (kmph)', ylabel='V2')
    ax.label_outer()

plt.legend(title="Track layer", bbox_to_anchor=(0.72,-0.28),
           fontsize=10, ncol=3, bbox_transform=plt.gcf().transFigure)
plt.subplots_adjust(left=None, bottom=-0.2, right=None, top=None, wspace=None, hspace=None)
plt.show()  
fig.savefig('destination_path.eps', bbox_inches="tight",format='eps', dpi=1000) 