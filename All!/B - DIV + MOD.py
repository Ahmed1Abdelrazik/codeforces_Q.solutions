#Abdelrazik
 
Q = int(input())
W = []
f = 0
for i in range(Q):
    W= list(map(int, input().split()))
    f = i
    if W[1]%W[2] ==0 and W[0] != W[1]:
        print(max(( (W[1]-1) // W[2] )+ (W[1]-1) % W[2],(W[1]) // W[2] )+ (W[1]) % W[2] )
 
    elif W[0] == W[1]:
        print(W[1]//W[2]+ W[1]%W[2])
 
    else:
        if W[1] - (W[1]%W[2]) -1 >= W[0] and ((W[1]%W[2])) != W[2]-1 :
            print(( (W[1] - W[1]%W[2] -1) // W[2] ) + (W[1] - W[1]%W[2] -1) % W[2]  )
 
 
        else:
            print( W[1] // W[2] + W[1] % W[2])