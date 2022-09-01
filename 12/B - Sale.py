#Ahmed Abdelrazik
n,m = map(int,input().split())
A = list(map(int,input().split()))
c = 0
MM = []
for i in range(n):
    if A[i]<0: MM.append(abs(A[i]))
 
MM.sort(reverse=True)
 
print(sum(MM[:m]))