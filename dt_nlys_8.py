import os
import pandas as pd
import matplotlib.pyplot as plt
#from sklearn import metrics
#from matplotlib.ticker import FormatStrFormatter as fsf
#from plottr_8_1 import plottr_8
from read_n_plot import read_8,subPlotter_8

os.chdir(os.path.dirname(os.path.abspath(__file__))+'/s22/std_2_8')

def all_cases(lyr,quant):
    fls = ['ic','ie','xc','xe']
    spd = [0,25,50,75,100,125,150,175,200]
    dt = []
    for i in fls:
        flnm = i+'_'+lyr
        fls[len(dt)]=flnm
        dt.append(read_8(flnm,quant))
    fls.insert(0,'speed_'+quant)
    df = pd.DataFrame(list(zip(spd,dt[0],dt[1],dt[2],dt[3])), columns =fls)
    return df

print(all_cases('blt_','area'))

b = ['blt_','sbt_','sbg_']
fig, sub_axs = plt.subplots(nrows=3, ncols=1)#, sharex=True, sharey=True, figsize=(9, 6))
for j in range(len(b)):
    subPlotter_8(all_cases(b[j],'area'),j,sub_axs)

for ax in sub_axs.flat:
    ax.set(xlabel='Speed (kmph)', ylabel='V2')
    ax.label_outer()

plt.legend(title="Load configuration", bbox_to_anchor=(0.9,-0.3),
           fontsize=10, ncol=4, bbox_transform=plt.gcf().transFigure)
plt.subplots_adjust(left=None, bottom=-0.2, right=None, top=None, wspace=None, hspace=None)
plt.show()  
fig.savefig('destination_path.eps', bbox_inches="tight",format='eps', dpi=1000) 