#Abdelrazik
from operator import itemgetter
# s is the strength
# n is levels
def Dragons(s,n):
    Strength = s
 
    List_of_IN = []
    for i in range(n):
        Q = list(map(int,input().split()))
 
 
        List_of_IN.append(Q)
    List_of_IN.sort(key=itemgetter(0))
 
    for i in range(n):
        if Strength <= List_of_IN[i][0]:
            return "NO"
        else:
            Strength += List_of_IN[i][1]
 
    return "YES"
 
 
 
 
 
W = list(map(int,input().split()))
s, n = W[0],W[1]
 
print(Dragons(s,n))
 
 