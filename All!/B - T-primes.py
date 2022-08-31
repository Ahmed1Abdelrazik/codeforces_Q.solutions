# Ahmed_Abdelrazik
# T_Primes : 4, 9, 25 , ..., p^2
 
from math import sqrt,ceil
 
def primes_less_than(n: int):
    if n<= 2:
        return []
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
 
    for i in range(2, ceil(sqrt(n))+1):
        if is_prime[i]:
            for x in range(i*i, n, i):
                is_prime[x] = False
 
    return [i**2 for i in range(n) if is_prime[i]]
 
 
T_Primes = set(primes_less_than(10**6+1))
 
def Solution(n):
    # if its not in 24 T +1 form it is not T_prime ...[1]
    # else checking if its in T_primes or not
 
    for r in list(map(int, input().split())):
        #from [1] Theorem
        if r % 24 != 1 and r > 9:
            print("NO")
        ### checking if r is T_prime
        else:
            if r in T_Primes:
                print("YES")
            else:
                print("NO")
 
 
n = int(input())
Solution(n)