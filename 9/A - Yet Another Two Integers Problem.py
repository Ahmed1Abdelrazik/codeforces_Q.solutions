# Ahmed Abdelrazik
 
t= int(input())
while t:
    a,b = map(int,input().split())
    print(abs(a-b)//10 + 1 if abs(a-b)%10 !=0 else abs(a-b)//10  )
    t -=1