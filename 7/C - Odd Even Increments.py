# Ahmed_Abdelrazik
 
t = int(input())
 
for q in range(t):
    n = int(input())
    Q = list(map(int, input().split()))
    f = True
    Evens = []
    Odds = []
    for i in range(n):
        if i%2==0:
            Evens.append(Q[i])
        else:
            Odds.append(Q[i])
    if n >2:
        for i in range(len(Evens)-1):
 
            if Evens[i] % 2 == 0 and Evens[i + 1] % 2 != 0:
                print("NO")
                f= False
                break
            if Evens[i] % 2 != 0 and Evens[i + 1] % 2 == 0:
                print("NO")
                f = False
                break
        if f == True:
            for i in range(len(Odds)-1):
                if Odds[i] % 2 == 0 and Odds[i + 1] % 2 != 0:
                    print("NO")
                    break
                if Odds[i] % 2 != 0 and Odds[i + 1] % 2 == 0:
                    print("NO")
                    break
            else:
                print("YES")
    else:
        print("YES")