#Ahmed Abdelrazik
 
Teams = {}
for _ in range(int(input())):
    L = input()
    if L not in Teams: Teams[L]=1
    else: Teams[L]+=1
 
print(  list(Teams.keys())[list(Teams.values()).index(max(Teams.values()))])