#Abdelrazik
 
def Percent(n):
    W = list(map(int,input().split()))
    m=0
    for q in range(n):
       m += float(W[q] /100)
 
    return float(m/n * 100)
 
 
n = int(input())
 
print(Percent(n))