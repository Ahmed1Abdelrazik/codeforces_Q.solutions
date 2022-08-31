# Ahmed_Abdelrazik
from math import factorial
t =int(input())
 
 
for i in range(t):
    n = int(input())
    if n%2 == 0:
        print(factorial(int(n/2))**2 % 998244353)
    else:
        print(0)