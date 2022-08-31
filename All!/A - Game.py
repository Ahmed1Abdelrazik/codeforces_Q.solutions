#Abdelrazik
T_cases = int(input())
 
for i in range(T_cases):
    n = int(input())
    Location =list(map(int, input().split()))
    G = list(Location)
    G.reverse()
 
    if 0 in Location:
        print((n-G.index(0)+1)-(Location.index(0)) )
 
    else:
        print(0)