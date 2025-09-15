count=0
leap=1

from math import sqrt

for i in range(101,150):
    k=int(sqrt(i+1))
    for j in range(2,k+1):
        if i%j==0:
            leap=0
            break
    if leap==1:
        print('%-4d'%i)
        count+=1
    leap=1
print('101~150之间素数的数量=%d'%count)
