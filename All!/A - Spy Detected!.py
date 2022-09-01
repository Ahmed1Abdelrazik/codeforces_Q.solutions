#TLE
 
for _ in range(int(input())):
    n =int(input())
    W = list(map(int,input().split()))
    for q in range(n):
        if W.count(W[q]) ==1:
            print(q+1)
            break