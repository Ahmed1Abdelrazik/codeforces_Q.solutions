# Ahmed Abdelrazik
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    f = True
    for i in range(n):
        if a[i] != i+1 and f==True:
            e = a.index(i+1)
            a = a[:i] + a[i:e+1][::-1] + a[e+1:]
            break
    print(*a)