#Abdelrazik
def Queue(a,b, Txt):
    L = []
 
    for i in range(a):
        L.append(Txt[i])
 
    for x in range(b):
        B = []
        for q in range(a):
            if L[q] == 'B':
                B.append(q)
 
 
 
        for j in range(len(B)):
 
            if B[j]+1 < len(L):
                if L[B[j]+1] == "G":
                    L[B[j]+1] = "B"
                    L[B[j]] = "G"
 
    return "".join(L)
 
W = list(map(int,input().split()))
Txt = input()
a,b = W[0], W[1]
 
print(Queue(a,b,Txt))