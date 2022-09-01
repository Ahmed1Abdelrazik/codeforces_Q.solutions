#Ahmed Abdelrazik
from itertools import permutations
import sys
sys.setrecursionlimit(4025)
 
def Sum(target, list, Dp = None):
    #Dp
    if Dp == None:
        Dp ={}
    if target in Dp:
        return Dp[target]
    #brute force
    if target ==0:
        return []
    if target < 0:
        return None
 
    for k in list:
        reminder = target - k
        reminderR = Sum(reminder,list,Dp)
        if reminderR != None:
            reminderR.append(k)
            Dp[target] = reminderR
            #print(Dp)
            return Dp[target]
 
    Dp[target] = None
    return None
 
n,a,b,c = map(int,input().split())
perm = permutations([a,b,c],3)
q = 0
for permutation in perm:
    p = len(Sum(n,list(permutation)))
    if p > q:
        q = p
 
print(q)
# print(len(Sum(n,[min(a,b,c),a+b+c- min(a,b,c)-max(a,b,c),max(a,b,c)])))