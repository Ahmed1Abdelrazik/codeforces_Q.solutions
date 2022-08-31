Q = int(input())
integers = input().split()
 
Z = Q
 
Serejia = 0
Dima = 0
for i in range(Q):
 
    if len(integers) != 1 and len(integers) != 0:
        if int(integers[0]) > int(integers[Q-1]):
            Serejia += int(integers[0])
            integers.remove(integers[0])
            Q -= 1
        else:
            Serejia += int(integers[Q-1])
            integers.remove(integers[Q-1])
            Q -= 1
        if int(integers[0])> int(integers[Q-1]) or len(integers) == 1:
            Dima += int(integers[0])
            integers.remove(integers[0])
            Q -= 1
        else:
            Dima += int(integers[Q-1])
            integers.remove(integers[Q-1])
            Q -= 1
if len(integers) == 1:
    Serejia += int(integers[0])
 
print(str(Serejia) + " " + str(Dima))