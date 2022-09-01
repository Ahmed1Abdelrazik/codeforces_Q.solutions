# Ahmed Abdelrazik
Alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
from itertools import combinations
 
 
def deff(word1,word2,l):
    s = 0
    for q in range(l):
        s += abs(Alpha.index(word1[q])-Alpha.index(word2[q]))
 
    return s
 
 
 
 
t= int(input())
for _ in range(t):
    n,m = map(int,input().split())
 
    W = []
    for __ in range(n):
        W.append(input())
    perm = combinations(W, 2)
    min = 100000
    for i in list(perm):
        u = deff(i[0], i[1], m)
        if u < min: min = u
 
    print(min)
 