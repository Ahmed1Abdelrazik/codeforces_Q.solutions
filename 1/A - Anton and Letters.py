#Strings always win!
L = input()
L=L.replace('{','')
L= L.replace('}','')
L = L.replace(', ','')
 
Q = len(L)
n = 0
for i in L:
 
    if L.count(i) >1:
        n += L.count(i)-1
    L =  L.replace(i,'')
 
print(Q-n)