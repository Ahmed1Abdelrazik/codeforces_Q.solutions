# Ahmed Abdelrazik
 
for _ in range(int(input())):
    n = int(input())
    A = list(sorted(map(int,input().split())))
    min = 104450120
    for j in range(n-1):
        V = A[j+1]-A[j]
        if V<min: min = V
 
    print(min)