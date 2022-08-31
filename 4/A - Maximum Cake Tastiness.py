#Abdlerazik
 
def THE_TAST(n):
    Output = []
    for i in range(n):
        a = int(input())
        list_of_cakes = list(map(int, input().split()))
        max1 = max(list_of_cakes)
        list_of_cakes.pop(list_of_cakes.index(max1))
        max2 = max(list_of_cakes)
        Output.append(max1+max2)
 
    for i in range(len(Output)):
        print(Output[i])
 
 
 
 
n = int(input())
THE_TAST(n)