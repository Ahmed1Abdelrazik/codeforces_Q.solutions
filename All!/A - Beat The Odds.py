# Ahmed_Abdelrazik
 
for _ in range(int(input())):
    n = int(input())
    odds = 0
    evens = 0
    for a in map(int,input().split()):
        if a%2==0: evens+=1
        else: odds+=1
 
    print(min(odds,evens))