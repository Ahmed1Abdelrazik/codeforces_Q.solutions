##List of lists!
Q = int(input())
result =0
_lists = []
for i in range(Q):
    _lists.append(input().split())
    
for k in range(Q):
    for i in range(Q):
            if _lists[0][0] == _lists[i][1]:
                result+=1
            if _lists[0][1] == _lists[i][0]:
                result += 1
    _lists.pop(0)
    _lists.append([str(0),str(0)])
print(result)