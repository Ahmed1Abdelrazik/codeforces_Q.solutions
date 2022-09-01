#Abdelrazik
 
t = int(input())
 
for i in range(t):
    n = int(input())
    E = list(map(int,input().split()))
    E.sort()
    for i in range(1,n):
        if E[i]-E[i-1]>1:
            print("NO")
            break
    else:
        print("YES")