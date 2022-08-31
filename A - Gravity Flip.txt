 
Columns = int(input())
A1 = input().split()
A=[]
for a in range(Columns):
    A.append(int(A1[a]))
#A.insert(1, 52)
#A.pop(2)
 
#print(A)
 
for x in range(len(A)):
    for i in range(Columns-1):
 
        if int(A[i]) > int(A[i+1]):
            j = A[i] - A[i + 1]
            A[i+1]= A[i+1]+(j)
            #print(A)
            A[i] = A[i] - (j)
            #print(A)
 
for z in range(Columns):
    print(A[z], end=" ")
