import sys as s
import numpy as np
 
data = np.loadtxt(s.argv[1], delimiter='\n', dtype=np.int)

perc = np.percentile(data, 90)
med = np.median(data)
maximum = max(data)
minimum = min(data)
mean_v = np.mean(data)

print("%.2f" % perc)
print("%.2f" % med)
print("%.2f" % maximum)
print("%.2f" % minimum)
print("%.2f" % mean_v)
