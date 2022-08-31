#Abdelrazik
 
def Solve_Lo2lo2a(n):
    for i in range(n):
        q = int(input())
        if q%4 ==0 :
            print("YES")
            for r in range(2,q+2,2):
                print(r, end =" ")
            for r in range(2, q+4, 2):
                if r != int(q/2 +2):
                    print(r-1, end=" ")
            print()
        else:
            print("NO")
 
 
n = int(input())
Solve_Lo2lo2a(n)