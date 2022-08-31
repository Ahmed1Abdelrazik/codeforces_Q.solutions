#Abdelrazik
 
def Good_Pairs(n):
 
    for i in range(n):
        a = int(input())
        W = list(map(int,input().split()))
        print( W.index(min(W))+1, W.index(max(W))+1)
 
 
n = int(input())
 
Good_Pairs(n)