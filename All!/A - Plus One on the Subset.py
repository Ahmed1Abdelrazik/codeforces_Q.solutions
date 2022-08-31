#Abdelrazik
Q = int(input())
W = []
for i in range(Q):
    n = int(input())
    W.append(list(map(int, input().split())))
 
for i in range(Q):
    print(max(W[i])-min(W[i]))