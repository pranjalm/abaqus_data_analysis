def plottr_8(flnm):
    fls=sorted([fl for fl in os.listdir(".") if flnm in fl])
    df = pd.read_csv(fls[0], sep="\s+",engine='python', header=0)
    df2 = pd.read_csv(fls[1], sep="\s+",engine='python', header=0)
    df3 = pd.read_csv(fls[2], sep="\s+",engine='python', header=0)
    df4 = pd.read_csv(fls[3], sep="\s+",engine='python', header=0)
    df5 = pd.read_csv(fls[4], sep="\s+",engine='python', header=0)
    df6 = pd.read_csv(fls[5], sep="\s+",engine='python', header=0)
    df7 = pd.read_csv(fls[6], sep="\s+",engine='python', header=0)
    df8 = pd.read_csv(fls[7], sep="\s+",engine='python', header=0)
    df9 = pd.read_csv(fls[8], sep="\s+",engine='python', header=0)
    plott = plt.figure()
    plt.plot(df.iloc[:,0],df.iloc[:,1], marker='', markerfacecolor='blue', 
             markersize=2, color='black', linewidth=2, linestyle=':', label="0")
    plt.plot(df2.iloc[:,0],df2.iloc[:,1], marker='', markerfacecolor='blue', 
             markersize=2, color='black', linewidth=2, linestyle='--', label="25")
    plt.plot(df3.iloc[:,0],df3.iloc[:,1], marker='', markerfacecolor='blue', 
             markersize=2, color='black', linewidth=2, linestyle='-.', label="50")
    plt.plot(df4.iloc[:,0],df4.iloc[:,1], marker='.', markerfacecolor='black', 
             markersize=3, color='black', linewidth=1, linestyle='--', label="75")
    plt.plot(df5.iloc[:,0],df5.iloc[:,1], marker='', markerfacecolor='blue', 
             markersize=2, color='black', linewidth=2, linestyle='-.', label="100")
    plt.plot(df6.iloc[:,0],df6.iloc[:,1], marker='', markerfacecolor='blue', 
             markersize=2, color='black', linewidth=2, linestyle='-.', label="125")
    plt.plot(df7.iloc[:,0],df7.iloc[:,1], marker='', markerfacecolor='blue', 
             markersize=2, color='black', linewidth=2, linestyle='-.', label="150")
    plt.plot(df8.iloc[:,0],df8.iloc[:,1], marker='', markerfacecolor='blue', 
             markersize=2, color='black', linewidth=2, linestyle='-.', label="175")
    plt.plot(df9.iloc[:,0],df9.iloc[:,1], marker='', markerfacecolor='blue', 
             markersize=2, color='black', linewidth=2, linestyle='-.', label="200")
    
    plt.xlim(0,300)
    plt.xlabel('Distance along the path (m)')
    plt.ylabel('Vertical stress (Pa)')
    plt.ylabel('Vertical velocity (m/sec)')
    plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))    
    plt.legend(title="Speed (kmph)", loc='lower right')
    plt.tight_layout()
    plott.savefig('destination_path.eps', format='eps', dpi=1000)
    plt.show()