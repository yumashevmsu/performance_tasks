import numpy as np
import sys as s

q = []
with open(s.argv[1]) as f:
    for line in f:
        q.append([float(x) for x in line.split()])
		
points = []
with open(s.argv[2]) as f:
    for line in f:
        points.append([float(x) for x in line.split()])


		
for p in points:
    flag = False
    indicator = 3
	
    for qpoint in q:
	    if p == qpoint:
		    indicator = 0
		    flag = True
		    break
   
   
    if flag == False:
		
	    AT1 = (1/2)*abs((q[1][0] - q[0][0])*(p[1] - q[0][1]) - (p[0] - q[0][0])*(q[1][1]-q[0][1]))
	    AT2 = (1/2)*abs((q[2][0] - q[1][0])*(p[1] - q[1][1]) - (p[0] - q[1][0])*(q[2][1]-q[1][1]))
	    AT3 = (1/2)*abs((q[3][0] - q[2][0])*(p[1] - q[2][1]) - (p[0] - q[2][0])*(q[3][1]-q[2][1]))
	    AT4 = (1/2)*abs((q[0][0] - q[3][0])*(p[1] - q[3][1]) - (p[0] - q[3][0])*(q[0][1]-q[3][1]))
		
	    AQ = (1/2)*abs((q[0][0]*q[1][1]+q[1][0]*q[2][1]+q[2][0]*q[3][1]+q[3][0]*q[0][1]-q[1][0]*q[0][1]-q[2][0]*q[1][1]-q[3][0]*q[2][1]-q[0][0]*q[3][1]))
		
		
	    if (AQ == AT1 + AT2 + AT3 + AT4):
		    indicator = 2
		
	    if ((AT1 == 0) or (AT2 == 0) or (AT3 == 0) or (AT4 == 0)) and (indicator == 2):
		    indicator = 1
		
		
		
    print(indicator)