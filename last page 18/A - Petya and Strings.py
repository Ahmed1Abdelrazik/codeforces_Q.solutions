S1 = input()
S2 = input()
 
result = 0
 
if S1.lower() < S2.lower() :
    print(-1)
elif S1.lower() > S2.lower():
    print(1)
else:
    print(0)