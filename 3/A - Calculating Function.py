#Abdelrazik
 
def Function(n):
    if n %2 ==0 :
        return int(n/2)
    else: return - int((n+1)/2)
 
n = int(input())
 
print(Function(n))