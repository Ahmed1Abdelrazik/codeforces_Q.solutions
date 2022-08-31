#Abdelrazik
n = input()
VVV = 0
Luckey_numbers = [4, 7, 44, 47, 74, 474, 444, 447,477 ]
 
for k in range(9):
    if int(n) % Luckey_numbers[k] == 0:
        VVV = 1
        print("YES")
        break
    else:
        continue
 
if VVV == 0:
    print("NO")