#Abdelrazik
 
def Signs():
    W = [a,b,c]
 
    if W[0]== W[1] == W[2] == 1 or   W[0]== W[2] ==1:
        return (W[0]+W[1]+W[2])
    elif W[0] == 1 and W[2] != 1:
        return (W[0]+W[1])*W[2]
    elif W[1] == 1 and W[0] != 1:
        if W[0]>W[2]:
            return W[0]*(W[1]+W[2])
        else:
            return (W[0] +W[1]) * W[2]
    elif W[2] == 1 and W[0] != 1:
        return W[0]*(W[1]+W[2])
    return (W[0] * W[1]) * W[2]
 
a = int(input())
b = int(input())
c = int(input())
 
print(Signs())