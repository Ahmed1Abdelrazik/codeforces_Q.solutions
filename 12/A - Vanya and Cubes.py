#Ahmed Abdelrazik
 
n = int(input())
i = 1
lvl = 0
while n>=(i*(i+1)/2):
    n -= i*(i+1)/2
    i+=1
    lvl+=1
print(lvl)