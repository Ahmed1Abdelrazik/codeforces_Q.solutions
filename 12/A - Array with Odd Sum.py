#Ahmed Abdelrazik
 
for _ in range(int(input())):
        n = int(input())
        A = map(int,input().split())
        even = False
        odd = False
        for a in A:
            if a%2==0: even = True
            else: odd = True
 
        if even ==True and odd== True: print("YES")
        elif even == False and odd == True:
            if n%2 ==0: print("No")
            else: print("Yes")
 
        else:
            print("NO")
 
 
 