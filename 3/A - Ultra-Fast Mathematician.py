#Abdelrazik
 
def Ultra(n,m):
    Q =''
    for i in range(len(n)):
        if n[i] != m[i]:
            Q +=str(1)
        else:
            Q+=str(0)
 
    return Q
 
n = input()
m = input()
print(Ultra(n,m))