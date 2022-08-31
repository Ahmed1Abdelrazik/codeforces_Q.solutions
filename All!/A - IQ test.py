#Abdelrazik
 
def IQ_test(a):
    W= list(map(int,input().split()))
 
    E = []
 
    for i in range(a):
        E.append(W[i] %2)# 1 or 0 for even
 
    Even_odd = max(set(E), key = E.count)
    if Even_odd == 0:
        for q in range(a):
            if W[q]%2 == 1:
                return q+1
    else:
        for q in range(a):
            if W[q]%2 == 0:
                return q+1
 
a = int(input())
print(IQ_test(a))
