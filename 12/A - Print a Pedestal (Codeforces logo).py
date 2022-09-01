#Ahmed Abdelrazik
 
for _ in range(int(input())):
        n= int(input())
        if n%3 ==0:
            print(n//3 ,n//3 +1,n//3 -1 )
        elif n%3 == 1 :
            if n==7:
                print(2,4,1)
            else:
                print(n//3+1,n//3+2,n//3 -2 )
        else:
 
            print(n//3+1,n//3+2,n//3 -1)