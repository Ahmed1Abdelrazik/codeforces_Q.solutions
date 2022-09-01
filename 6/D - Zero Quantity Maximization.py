#Ahmed_Abdelrazik
from collections import Counter
from decimal import Decimal
def Most_Common(List):
    data = Counter(List)
    return List.count(data.most_common(1)[0][0])
 
n = int(input())
In1 = list(map(int,input().split()))
In2 =list(map(int,input().split()))
 
i = 0
List_of_Div = []
zerobyzero = 0
while i<n:
    if In1[i] == 0 :
        if In2[i] == 0:
            zerobyzero += 1
        else:
            i+=1
            continue
    elif In2[i] ==0:
        List_of_Div.append(0)
    else:
        List_of_Div.append((Decimal(In1[i]) / Decimal(In2[i])))
    i+=1
 
 
if len(List_of_Div)>0:
    print(Most_Common(List_of_Div)+zerobyzero)
else:
    print(0 + zerobyzero)