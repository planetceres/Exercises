import math
import os
import time

integerarray = open(r'[array].txt', 'r')
integerarray = list(integerarray)

integerarray = list(map(int, integerarray))
print(len(integerarray))

t0 = time.time()
a = integerarray
n = len(a)
ax = math.floor(len(a)/2)
left = a[0:ax]
right = a[ax:]
a1 = []
b1 = []

def sort_side(side, inversions):
    newvalue = []
    while side:
        min=side[0]
        for i in side:
            if (i < min):
                min = i
        inversions += side.index(min)
        newvalue.append(min)
        side.remove(min)
    return newvalue, inversions
    
print("Sorting sides...")
t1 = time.time()    
inversions = 0    
a1, inversions = sort_side(left, inversions)
print('Sorted A in: %3f' % (time.time()-t1))
t1 = time.time() 
b1, inversions = sort_side(right, inversions)
print('Sorted B in: %3f' % (time.time()-t1))

c = []
k=0
i=0
j=0
for k in range(n):
	la1 = len(a1)
	lb1 = len(b1)
	if (0 <= i < la1) & (0 <= j < lb1):
		if a1[i] < b1[j]:
			c.append(a1[i])
			i += 1
		else:
			inv = len(a1[i:])
			inversions += inv
			c.append(b1[j])
			j += 1
	else:
	    if (0 <= i < la1):
	        remain = a1[i:]
	    else:
	        remain = b1[j:]
	    c = c + remain
	    break
print('Total inversions: %d' % inversions)
print('Time: %3f' % (time.time()-t0))

