#Abdelrazik
n,m = map(int,input().split())
 
for i in range(n//2):
    if i%2 == 0:
        print("#"*m)
        print("."*(m-1)+"#")
    else:
        print("#" * m)
        print("#"+ "." * (m - 1))
print("#"*m)