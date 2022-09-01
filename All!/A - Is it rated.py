# Ahmed_Abdelrazik
 
Q = int(input())
W = []
 
for i in range(Q):
    W.append(list(map(int, input().split())))
 
signal = True
for k in range(Q):
    if W[k][0] != W[k][1]:   #[ [a1 ,b1] , [a2, b2], [a3, b3] ]
        print("rated")
        signal = False
        break
 
 
if signal == True:
    for i in range(Q-1):
        if W[i][0]<W[i+1][0]:
            print("unrated")
            break
    else:
        print("maybe")