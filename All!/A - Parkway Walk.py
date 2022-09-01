#Ahmed Abdelrazik
 
t = int(input())
for _ in range(t):
    n,m  = map(int,input().split())
    A = list(map(int,input().split()))
    S = sum(A)
    print(S-m if S>=m else "0" )