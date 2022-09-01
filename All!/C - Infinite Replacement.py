# Ahmed Abdelrazik
 
t = int(input())
for i in range(t):
    s = input()
    t = input()
 
    if len(t) > 1 and "a" in t:
        print(-1)
 
    elif len(t) >1 and "a"not in t:
        count = s.count(t)
        print(2 ** (len(s)))
    else:
        count = s.count(t)
        print(2**(len(s)-count))