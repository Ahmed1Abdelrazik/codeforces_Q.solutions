
#Strings always win!
Q= int(input())
W= []
for q in range(Q):
    W.append(input())
 
for i in W:
    if len(i)>10:
        print(i[0]+str(len(i)-2)+i[len(i)-1])
    else:
        print(i)