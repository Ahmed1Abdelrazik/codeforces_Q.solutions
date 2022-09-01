# Ahmed Abdelrazik
 
twos= []
for q in range(2,32):
    twos.append(2**q-1)
 
for _ in range(int(input())):
    n = int(input())
 
    for b in twos:
        if n % b ==0:
            print(n//b)
            break