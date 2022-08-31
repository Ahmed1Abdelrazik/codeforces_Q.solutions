#Abdelrazik
 
def Subtract(t):
    for i in range(t):
        N_and_K = list(map(int, input().split()))
        n,k =N_and_K[0],N_and_K[1]
        INPUT = list(map(int,input().split()))
        Set = set(INPUT)
        p = 0
        for i in range(n):
            if INPUT[i] + k in Set:
                print("YES")
                p = 1
                break
        if p ==0:
            print("NO")
 
 
 
t =int(input())
Subtract(t)