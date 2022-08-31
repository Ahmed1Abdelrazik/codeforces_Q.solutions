#Abdelrazik
 
def lanterns(n,l):
    W = list(map(int,input().split()))
    W.sort()
    max_empty = 0
    for q in range(1,n):
        if W[q] - W[q-1] > max_empty:
            max_empty = W[q] - W[q-1]
 
    return max(max_empty/2, W[0], l - W[n-1])
 
 
Input = list(map(int,input().split()))
n,l = Input[0],Input[1]
print(lanterns(n,l))