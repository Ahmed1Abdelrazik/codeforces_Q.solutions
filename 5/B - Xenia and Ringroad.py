#Abdelrazik
 
n,m = map(int,input().split())
 
W = list(map(int,input().split()))
count = W[0]-1
for i in range(1,m):
    if W[i]<W[i-1]:
        count += n - W[i-1] + W[i]
    else:
        count += W[i] - W[i-1]
 
print(count)