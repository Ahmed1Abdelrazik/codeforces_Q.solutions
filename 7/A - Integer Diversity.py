#Ahmed_Abdelrazik
 
q = int(input())
 
for i in range(q):
    n = int(input())
    W = list(map(int, input().split()))
    Dic = {}
    for m in range(n):
        if abs(W[m]) in Dic and W[m]!=0:
            Dic[abs(W[m])]+=1
        else:
            Dic[abs(W[m])] = 1
 
    M = 0
    for k in Dic:
        if Dic[k]>1:
            M += 2
        else:
            M +=1
    print(M)