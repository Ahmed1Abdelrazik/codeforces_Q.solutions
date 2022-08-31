#Abdelrazik
Q = int(input())
 
Year = 0
for i in range(Q+1,10000):
    VVV = 0
    for k in range(3):
        if str(i)[k] in str(i)[k+1:]:
            VVV =1
            break
        else:
            continue
    if VVV == 0:
        print(i)
        break