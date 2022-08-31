#Abdelrazik
q = input()
w = input()
 
Q =[]
W =[]
for i in range(min(len(q),len(w))):
    Q.append(q[i])
    W.append(w[i])
 
Q.reverse()
if Q == W:
    print("YES")
else:
    print("NO")