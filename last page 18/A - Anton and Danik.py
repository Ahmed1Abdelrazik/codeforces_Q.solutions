
n = int(input())
Word = input()
 
Anton  = 0
Danik = 0
for x in Word:
    if x == "A":
       Anton = Anton+1
    else:
       Danik = Danik + 1
 
if Anton > Danik:
    print("Anton")
elif Danik > Anton:
    print("Danik")
else:
    print("Friendship")
 