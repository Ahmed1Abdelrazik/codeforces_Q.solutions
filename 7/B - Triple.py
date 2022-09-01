#Ahmed_Abdelrazik
 
from collections import Counter
 
 
t = int(input())
 
for i in range(t):
    n = int(input())
    w = list(map(int,input().split()))
    Dic = {}
    for q in range(n):
        if w[q] not in Dic:
            Dic[w[q]]=1
        else:
            Dic[w[q]]+=1
 
    for k in Dic:
        if Dic[k]>= 3:
            print(k)
            break
    else:
        print(-1)