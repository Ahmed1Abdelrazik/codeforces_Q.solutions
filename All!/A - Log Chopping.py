#Ahmed_Abdelrazik
 
def Div(W,n):
    count = 0
    return sum(W)-n
 
#Solution
t= int(input())
for q in range(t):
    n =int(input())
    N = map(int,input().split())
    H = Div(N,n)
 
    if H%2:
        print("errorgorn")
    else:
        print("maomao90")