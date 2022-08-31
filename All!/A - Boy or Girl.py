Q = input()
E =""
W = 0
for i in Q:
    if i in E:
        W +=0
 
    else:
        W += 1
        E = E + str(i)
 
if W %2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")