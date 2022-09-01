# Ahmed Abdelrazik
from math import ceil
n,k = map(int,input().split())
 
for i in range(ceil(n/2),n+1):
    if i %k==0:
        print(i)
        break
else:print(-1)