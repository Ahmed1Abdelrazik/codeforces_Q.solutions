# Ahmed_Abdelrazik
import bisect
t = int(input())
 
for _ in range(t):
    n,q = map(int,input().split())
    Q = list(map(int,input().split()))
    Q.sort(reverse=True)
 
    Sum = [Q[0]]
    for j in range(1,n):
        Sum.append(Sum[j-1]+Q[j])
 
 
    for i in range(q):
        x = int(input())
        print(bisect.bisect_left(Sum, x)+1 if x <=Sum[-1] else -1)