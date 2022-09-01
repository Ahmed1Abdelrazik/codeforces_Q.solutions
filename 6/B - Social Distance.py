#Ahmed_Abdelrazik
 
t = int(input())
 
 
for q in range(t):
    n,m = map(int,input().split())
    Array = list(map(int,input().split()))
    Array.sort(reverse=True)
    Sum = 0
    for i in range(n):
        if i ==0:
            Sum+=2*Array[i]
        elif i != n-1:
            Sum+=Array[i]
    #print(Sum,abs(n-m))
    if Sum <= abs(n-m):
        print("YES")
    else:
        print("NO")