 
 
A1 = input().split()
A2 = input().split()
A3 = input().split()
A4 = input().split()
A5 = input().split()
 
result= ""
place = 0
for i in range(5):
    result = result+A1[i]+ A2[i]+A3[i]+A4[i]+A5[i]
for l in range(len(result)):
    if result[l] == '1':
        place = int(l)+1
if (place) % 5 != 0:
    the_Min = abs(3-(place % 5)) + abs(3-((place//5)+1))
 
else:
    the_Min = int(2 + abs(3-((place/5))))
#print(place)
#print(place%5)
#print((place // 5)+1)
 
print(the_Min)
 
 
 
 