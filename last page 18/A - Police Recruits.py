Q = int(input())
Recruits = input().split()
result = 0
hired = 0
for k in range(len(Recruits)):
    if Recruits[0] == "-1":
        if hired == 0:
            result += 1
            Recruits.pop(0)
        else:
            Recruits.pop(0)
            hired -= 1
    elif Recruits[0] != '-1':
        hired += int(Recruits[0])
        Recruits.pop(0)
print(result)
 