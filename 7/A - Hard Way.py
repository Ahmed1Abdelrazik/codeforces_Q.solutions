# Ahmed_Abdelrazik
 
for k in range(int(input())):
    tringle = []
    for i in range(3):
        tringle.append(list(map(int,input().split())))
 
    #print(tringle)
 
    if tringle[0][1] == tringle[1][1]   and tringle[2][1] < tringle[0][1]:
        print( abs(tringle[0][0] - tringle[1][0]) )
 
    elif tringle[0][1] == tringle[2][1] and tringle[1][1] < tringle[0][1]:
        print( abs(tringle[0][0] - tringle[2][0]) )
 
    elif tringle[1][1] == tringle[2][1] and tringle[0][1] < tringle[1][1]:
        print( abs(tringle[1][0] - tringle[2][0]) )
 
    else:
        print(0)