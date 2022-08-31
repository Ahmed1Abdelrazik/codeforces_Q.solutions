#Strings always win
W= str(input())
Q = str(input())
n = 0
for i in W:
    if i in Q:
        n+=1
        Q =Q[Q.index(i)+1:]
    else:
        break
 
print(n+1)