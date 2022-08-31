#Abdelrazik
 
[n,m,a] = list(map(int,input().split()))
 
 
if n %a ==0:
    a1 = n / a
else:
    a1 = n//a + 1
 
 
if m %a ==0:
    a2 = m/ a
else:
    a2 = m//a + 1
 
 
print(int(a1*a2))