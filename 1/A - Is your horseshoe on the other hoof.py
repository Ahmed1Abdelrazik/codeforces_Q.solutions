R = input().split()
W =""
for i in range(4):
    W += str(R[i])
 
n = 0
for i in R:
    if W.count(i) > 1:
        n += W.count(i)-1
        W = W.replace(i,"")
 
if n > 0:
    print(n)
else:
    print(0)