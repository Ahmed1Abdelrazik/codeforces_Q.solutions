#Abdelrazik
IN = []
for i in range(5):
    IN.append(int(input()))
 
count = 0
for i in range(1,IN[4]+1):
    for q in IN[:4]:
        if i % q ==0:
            count += 1
            break
 
print(count)