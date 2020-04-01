import numpy as np
import sys as s

intervals = []
with open(s.argv[1]) as f:
    for line in f:
        intervals.append([str(x) for x in line.split()])


curr_val = 0
max_val = 0
result = []
sorted_intervals = []
for elem in intervals:
	begin, end_ = elem
	sorted_intervals.append((begin, 1))
	sorted_intervals.append((end_, 0))

	
sorted_intervals = sorted(sorted_intervals)


for elem in sorted_intervals:
	if elem[1] == 1:
		curr_val += 1
	else:
		curr_val -= 1
	result.append((elem[0], curr_val))
	max_val = max(max_val, curr_val)


prev = 0
cut_result = []
for res in result:
    if (prev != 0):
        if (prev[0] == res[0]) and (res[1] == max_val):
	        cut_result.remove(prev)
    prev = res
    cut_result.append(res)

flag_begin = False
for res in cut_result:
    if (res[1] == max_val) and (flag_begin == False):
	    print(res[0], end = ' ')
	    flag_begin = True
	
    if (res[1] < max_val) and (flag_begin == True):
	    print(res[0])
	    flag_begin = False


