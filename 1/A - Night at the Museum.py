Q = input()
 
W = "abcdefghijklmnopqrstuvwxyz"
W1=''
result =0
 
for i in range(len(Q)):
    result += min(W.index(Q[i]),abs(26-W.index(Q[i])))
    W1= W[W.index(Q[i]):]+W[:W.index(Q[i])]
    W=W1
 
print(result)