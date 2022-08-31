#Abdelrazik
n = int(input())
S = []
Current = 0
for i in range(n):
    W = list(map(int,input().split()))
    Current = Current - W[0]+W[1]
    S.append(Current)
print(max(S))