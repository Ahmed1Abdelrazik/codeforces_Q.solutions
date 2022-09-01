#Ahmed_Abdelrazik
 
t = int(input())
W = list(map(int,input().split()))
Q = [0]*(t+1)
 
for q in range(t):
    Q[W[q]] = 1
    while Q[t]:
        print(t,end = " ")
        t -= 1
    if Q[t] !=1:
        print()