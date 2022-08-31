#Abdelrazik
 
t= int(input())
 
 
for i in range(t):
    n = int(input())
    Cos = input()
    Cos = Cos+" "
    zeros = 0
    count = 0
    for q in range(len(Cos)-1):
        if Cos[q] =="0" and Cos[q+1] == "0" :
            count += 2
        else:
            if Cos[q] =="0" and Cos[q+1] =="1" and Cos[q+2] =='0':
                count += 1
    print(count)