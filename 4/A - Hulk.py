#Abdelrazik
 
def I_hate(n):
    W = ['I hate','I love']*n
 
 
    return ' that '.join(W[:n]) + " it"
 
 
n = int(input())
 
print(I_hate(n))