Q = input().split()
W = input()
result = 0
for i in range(len(W)):
    result += int(Q[int(W[i])-1])
print(result)
