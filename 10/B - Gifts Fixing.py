# Ahmed Abdelrazik
 
for _ in range(int(input())):
    n = int(input())
 
    A = list(map(int,input().split()))
    minA = min(A)
    B = list(map(int,input().split()))
    minB = min(B)
 
 
    T = 0
    for j in range(n):
        T += min(A[j]-minA, B[j]-minB) + abs(A[j]-minA - B[j]+minB)
 
    print(T)