#Strings always win!
 
W = input().split()
(a,b) = (int(W[0]),int(W[1]))
Alphabet = 'qwertyuiopasdfghjklzxcvbnm'
 
 
password = ''
for j in range(int(a/b)):
    password+=Alphabet[:b]
 
if len(password)<a:
    password += Alphabet[:a-len(password)]
 
print(password)