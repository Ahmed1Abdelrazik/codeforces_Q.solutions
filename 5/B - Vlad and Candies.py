#Abdelrazik
 
t = int(input())
for i in range(t):
    n= int(input())
    W = list(map(int,input().split()))
    if n == 1:
        if W[0] <=1:
            print("Yes")
        else:
            print("NO")
    else:
        maximum1 = max(W)
        W.remove(maximum1)
        maximum2 = max(W)
        if abs(maximum1-maximum2) >1:
            print("NO")
        else:
            print("YES")