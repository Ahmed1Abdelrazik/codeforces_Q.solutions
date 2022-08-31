#Abdelrazik
q = 0
for i in range(int(input())):
    if input() in ["++X","X++"]:
        q += 1
    else:
        q -= 1
print(q)