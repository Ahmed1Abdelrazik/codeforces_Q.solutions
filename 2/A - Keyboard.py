#Abdelrazik
Char = input()
W = input()
 
Key1 = "qwertyuiopasdfghjkl;zxcvbnm,./"
Arranged_STR = ''
if Char == 'R':
    for i in W:
        Arranged_STR+= Key1[Key1.index(i)-1]
 
else:
    for i in W:
        Arranged_STR+= Key1[Key1.index(i)+1]
 
print(Arranged_STR)