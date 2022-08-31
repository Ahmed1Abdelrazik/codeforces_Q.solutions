#Strings always win!
W = input()
W1 =  []
for i in range(len(W)):
    if W[i] is not '+':
        W1.append(W[i])
 
for q in range(len(W1)):
 
    if int(W1[q]) == 1 :
        W1.insert(0,'1')
        W1.pop(q+1)
    elif int(W1[q]) == 3:
        W1.append(W1[q])
    else:
        continue
 
Three_numbers= W1.count('3')
 
for i in range(int(Three_numbers/2)):
    W1.remove('3')
 
print("+".join(i for i in W1))