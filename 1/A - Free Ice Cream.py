#Strings always win!
Q = input().split()
(Q1,Q2)= (int(Q[0]),int(Q[1]))
W= []
for q in range(Q1):
    W.append(input())
 
ice_creams_left = Q2
distressed_childs = 0
 
for i in range(Q1):
 
    if W[i][0]=='+':
        ice_creams_left += int(W[i][0]+W[i][2:])
    else:
        if int(W[i][2:])<= ice_creams_left:
            ice_creams_left -= int(W[i][2:])
        else:
            distressed_childs +=1
 
print(ice_creams_left,end = ' ')
print(distressed_childs,end = '')