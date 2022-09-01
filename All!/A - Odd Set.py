#Ahmed Abdelrazik
 
for _ in range(int(input())):
        n= int(input())
        A =map(int,input().split())
 
        odds = 0
        evens = 0
        for j in A:
            if j%2==0: evens+=1
            else: odds+=1
 
        print("Yes" if odds==evens else "No")