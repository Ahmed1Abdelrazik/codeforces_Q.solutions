#Abdelrazik
Q = int(input())
 
for f in range(Q):
    W = input()
    E = input()
    Y = ''
    for i in range(len(W)):
        if i % 2 ==0:
            Y +=W[i]
    if len(W) > 1:
        if E in Y:
            print("Yes")
        else:
            print("No")
    else:
        if W == E:
            print("Yes")
        else:
            print("No")