#Abdelrazik
 
def Solve_Lo2lo2a(n):
    for i in range(n):
        q = input()
 
        print(len(q)-q.count('0'))
        for r in range(0, len(q), 1):
            if q[r]!='0':
                print(int(q[r])*10**(len(q)-r-1), end=" ")
        print()
 
n = int(input())
Solve_Lo2lo2a(n)