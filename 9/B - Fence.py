# Ahmed Abdelrazik
 
n,k = map(int, input().split())
H = list(map(int,input().split()))
 
min = 0
index = 0
for i in range(k):
    min += H[i]
 
att = min
for q in range(1,n-k+1):
    att += -H[q-1] + H[q-1+k]
    if att < min:
        min = att
        index = q
 
print(index+1)