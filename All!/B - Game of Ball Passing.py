#Abdelrazik
T_cases = int(input())
 
for i in range(T_cases):
    n = int(input())
    Shoots =list(map(int, input().split()))
    maxi = max(Shoots)
    Shoots.remove(maxi)
    Sum = 0
    for q in Shoots:
        Sum += q
    if maxi - Sum <2 and maxi !=0 :
        print(1)
    elif maxi - Sum >=2:
        print(maxi-Sum)
    else:
        print(0)