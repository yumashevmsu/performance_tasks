import sys as s
import numpy as np
import statistics as st
 
data = np.loadtxt(s.argv[1], delimiter='\n', dtype=np.int)

perc = np.percentile(data, 90)

med = st.median(data)

maximum = max(data)

minimum = min(data)

mean_v = st.mean(data)

print("%.2f" % perc)
print("%.2f" % med)
print("%.2f" % maximum)
print("%.2f" % minimum)
print("%.2f" % mean_v)
