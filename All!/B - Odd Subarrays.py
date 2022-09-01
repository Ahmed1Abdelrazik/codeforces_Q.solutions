# Ahmed Abdelrazik
 
for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().split()))
    odd  = 0
 
    i =0
    while i<n-1:
        if A[i]>A[i+1]:
            odd+=1
            i+=2
        else:
            i+=1
    print(odd)