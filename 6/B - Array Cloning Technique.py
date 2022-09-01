#Ahmed_Abdelrazik
from collections import Counter
 
def Most_Common(List):
    data = Counter(List)
    return List.count(data.most_common(1)[0][0])
 
t= int(input())
 
for i in range(t):
 
    n = int(input())
    List = list(map(int,input().split()))
    c = Most_Common(List) #most common element
    eeee= n-c
    remain = n-c
    q = 0
    if n-c >0:
        while remain>0:
            remain -= c
            c *= 2
            q +=1
        #output = (n-c)+ int((n - c)/c)
 
            # 1 +
    if n == 1:
        print(0)
    else:
        print(eeee + q )