#Abdelrazik
R = int(input())
S = input().lower()
n= 1
 
Alpha = "qwertyuiopasdfghjklzxcvbnm"
for letter in Alpha:
    if S.count(letter) == 0:
        print("NO")
        n= 0
        break
    else:
        continue
if n ==1:
    print("YES")