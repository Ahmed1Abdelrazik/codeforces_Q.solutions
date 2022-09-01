# Ahmed Abdelrazik
t = int(input())
T =0
for i in range(t):
    word = input()
    if word[0]==  "T": T += 4
    if word[0] == "C": T += 6
    if word[0] == "O": T += 8
    if word[0] == "D": T += 12
    if word[0] == "I": T += 20
print(T)