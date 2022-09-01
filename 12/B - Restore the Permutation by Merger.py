#Ahmed Abdelrazik
t = int(input())
 
while t>0:
    t-=1
    n = int(input())
    A = list(map(int,input().split()))
    S = []
    for i in range(2*n):
        if A[i] not in S:
            print(A[i],end= " ")
            S.append(A[i])
 
    print()