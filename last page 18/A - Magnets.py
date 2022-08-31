Q = int(input())
Text= ""
for i in range(Q):
        x = input()
        Text += x
 
#print(Text)
 
count = 1
for z in range(len(Text)-1):
    if Text[z] == Text[z+1]:
        count += 1
print(count)