#Abdelrazik
 
def is_Easy(n):
    W = list(map(int,input().split()))
 
 
    if 1 in W:
        return "Hard"
 
    return "Easy"
 
n = int(input())
print(is_Easy(n))