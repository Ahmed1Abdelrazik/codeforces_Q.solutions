 
 
A = input().split(" ")
 
Limak = int(A[0])
Bob= int(A[1])
 
counter = 0
while Limak <= Bob :
    Limak = Limak * 3
    Bob = Bob * 2
    counter +=1
print(counter)
 