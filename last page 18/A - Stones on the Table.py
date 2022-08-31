Q = int(input())
Colors = input()
 
counts = 0
for i in range(Q-1):
    if Colors[i] == Colors[i+1]:
        counts += 1
print(counts)