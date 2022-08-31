#Abdelrazik
r = int(input())
h = 0
while h<r:
    a,b = map(int,input().split())
    if a%b!=0:
        print(b - a%b)
    else:
        print(0)
    h += 1