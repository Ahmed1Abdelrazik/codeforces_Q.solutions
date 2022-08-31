#Abdelrazik
 
def Cheap(n):
    if b < m * a :
        return min((n//m) * b + (n % m) * a, (n//m) * b + b)
    else:
        return n*a
 
INPUTS = list(map(int, input().split()))
n, m, a, b = INPUTS[0], INPUTS[1], INPUTS[2], INPUTS[3]
print(Cheap(n))