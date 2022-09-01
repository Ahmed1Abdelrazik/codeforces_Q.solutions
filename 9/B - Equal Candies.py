# Ahmed Abdelrazik
 
t= int(input())
 
for i in range(t):
    n = int(input())
    W = list(map(int,input().split()))
    m = min(W)
 
    T = 0
    for q in W:
        T+=q-m
 
    print(T)