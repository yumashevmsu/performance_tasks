import numpy as np
import sys as s

path = s.argv[1]

path1 = path+"\\Cash1.txt"
path2 = path+"\\Cash2.txt"
path3 = path+"\\Cash3.txt"
path4 = path+"\\Cash4.txt"
path5 = path+"\\Cash5.txt"
 
data1 = np.loadtxt(path1, delimiter='\n', dtype=np.float)
data2 = np.loadtxt(path2, delimiter='\n', dtype=np.float)
data3 = np.loadtxt(path3, delimiter='\n', dtype=np.float)
data4 = np.loadtxt(path4, delimiter='\n', dtype=np.float)
data5 = np.loadtxt(path5, delimiter='\n', dtype=np.float)

max_val = 0
interval = 0

for i in range(16):
    if data1[i]+data2[i]+data3[i]+data4[i]+data5[i] > max_val:
        max_val = data1[i]+data2[i]+data3[i]+data4[i]+data5[i]
        interval = i+1

print(interval)
