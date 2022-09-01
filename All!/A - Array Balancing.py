#Ahmed_Abdelrazik
 
t = int(input())
 
for i in range(t):
    n = int(input())
    A = list(map(int,input().split()))
    B = list(map(int, input().split()))
 
    A1=[]
    B1=[]
 
    for i in range(n):
        A1.append(min(A[i],B[i]))
        B1.append(max(A[i],B[i]))
 
    count = 0
    for q in range(1,n):
        count += abs( A1[q]-A1[q-1])
        count += abs(B1[q] - B1[q - 1])
    print(count)