### Strings always win!
Y = input().split()
Q = list(map(int, input().split()))     # The list of sizes of oranges
(n, b, d) = (int(Y[0]), int(Y[1]), int(Y[2]))
 
# Let's remove oranges that have a size > b
k =[]
for i in range(n):
    if Q[i] > b:
        k.append(i)
for q in range(len(k)):
    Q.pop(k[q]-q)
 
M = 0
A = 0
for c in Q:
    A += c
    if A > d:
        A = 0
        M += 1
 
print(M)