Q = input()
count = 0
for i in Q:
    if i.isupper():
        count +=1
    else:
        count +=0
if count > len(Q)/2:
    print(Q.upper())
else:
    print(Q.lower())