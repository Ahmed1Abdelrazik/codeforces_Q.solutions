# Ahmed Abdelrazik
from math import log2
for _ in range(int(input())):
        n = int(input())
        m = n
        count = 0
        while m%3==0:
                m = m/3
                count+=1
        e = 6**count / n
 
        if e.is_integer() == True:
                print(int(log2(e))+count)
        else:
                print(-1)