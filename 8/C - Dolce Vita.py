# Ahmed_Abdelrazik
 
 
def solution(n, x, W):
    result = 0
    sum = 0
    for q,t in enumerate(W):
        sum += t
        result += max(0,(x-sum)//(q+1)+1)
    return result
 
# taking inputs
t = int(input())
for q in range(t):
    n, x = map(int, input().split())
    W = sorted(map(int, input().split()))
    print(solution(n, x, W))