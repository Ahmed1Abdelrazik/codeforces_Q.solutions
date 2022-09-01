#Ahmed_Abdelrazik
 
for _ in range(int(input())):
    n =  int(input())
    L = list(map(str,input().split()))
    f = 1
    for q in range(len(L)-1):
        if L[q][1]!=L[q+1][0]:
            f = 0
            L.insert(q+1,L[q][1]+L[q+1][0])
    if f == 1:
        L.append(2*L[-1][1])
 
    #print(L)
 
    for q in range(len(L)):
        if q == 0:
            print(L[0], end="")
        else:
            print(L[q][1],end ="")
    print()