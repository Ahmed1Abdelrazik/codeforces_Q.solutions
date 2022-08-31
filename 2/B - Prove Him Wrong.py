#Abdelrazik
q = int(input())
 
def Our_Array(n):
    p = 1
    for i in range(n):
        print(p, end= ' ')
        p = 3*p
 
 
s=0
while s < q:
    n = int(input())
    if n <= 19:
        print("YES")
        Our_Array(n)
        print()
    else:
        print("NO")
    s+=1