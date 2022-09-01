#Ahmed_Abdelrazik
 
n = int(input())
W = list(map(int,input().split()))
 
TWO =[]
for i in range(1,16):
    TWO.append(2**i)
 
def twos(a):
    s= 0
    for i in range(a):
        if a%(2**i)==0:
            s=i
        else:
            break
    return s
 
def short(a):
    Q = []
    for i in  TWO:
        if i>a:
            Q.append(i-a)
            break
    return min(Q)
 
for a in W:
    E = []
    for i in range(15):
        E.append(15+i - twos(a+i))
    if a == 0:
        print(0, end = " ")
    else:
        print(min(E),end = " ")