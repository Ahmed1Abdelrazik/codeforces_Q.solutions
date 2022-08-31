#Abdelrazik
 
[n,k] = list(map(int,input().split()))
 
Q = list(map(int,input().split()))
 
out = 0
for i in range(n):
    if Q[i]>= Q[k-1] and Q[i] >0:
        out += 1
 
print(out)