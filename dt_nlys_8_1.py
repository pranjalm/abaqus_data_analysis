import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from matplotlib.ticker import FormatStrFormatter as fsf
import statsmodels.formula.api as sm
from plottr_8_1 import plottr_8
from read_n_plot import read_8
from read_n_plot import subPlotter_8_1 as subPlotter_8
#change directory to data
os.chdir(os.path.dirname(os.path.abspath(__file__))+'/s_max_princ/std_2_8')

def all_cases(cs,quant):
    fls = ['blt_','sbt_','sbg_']
    spd = [0,25,50,75,100,125,150,175,200]
    dt = []
    for i in fls:
        flnm = cs+'_'+i
        fls[len(dt)]=flnm
        dt.append(read_8(flnm,quant))
    fls.insert(0,'speed_'+quant)
    df = pd.DataFrame(list(zip(spd,dt[0],dt[1],dt[2])), columns =fls)
    return df

b = ['ic','ie','xc','xe']
df1 = []
for i in b:
    a = all_cases(i,'ptp')
    print(a.iloc[:,1:2],)
    df1.append(a.iloc[:,1:])
#df1 = pd.DataFrame(df1)
#print(df1)
## main function
def main():
    # print all cases
    #print(all_cases('ie','area'))
    #plotting subplots 
    b = ['ic','ie','xc','xe']
    fig, sub_axs = plt.subplots(nrows=4, ncols=1)#, sharex=True, sharey=True, figsize=(9, 6))
    for j in range(len(b)):
        subPlotter_8(all_cases(b[j],'area'),j, sub_axs)
    #changing axes properties
    for ax in sub_axs.flat:
        ax.set(xlabel='Speed (kmph)', ylabel='S22')
        ax.label_outer()
    #changing and positioning plot legend
    plt.legend(title="Load configuration", bbox_to_anchor=(0.8,-0.6),
            fontsize=10, ncol=4, bbox_transform=plt.gcf().transFigure)
    plt.subplots_adjust(left=None, bottom=-0.5, right=None, top=None, wspace=None, hspace=None)
    plt.show()
    #saving plot as eps file  
    fig.savefig('destination_path.eps', bbox_inches="tight",format='eps', dpi=1000) 

if __name__ == '__main__':
    main()