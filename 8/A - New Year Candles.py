# Ahmed_Abdelrazik
 
def hi(a,b):
    result = a
    while a>=b:
        result += a//b
        a = a//b + a%b
    return result
 
a,b = map(int,input().split())
print(hi(a,b))