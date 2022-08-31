###Strings always win!
 
n_lines = int(input())
####--------------------------------####
birds_number = list(map(int,input().split()))
n_shoots = int(input())
####--------------------------------####
pair_of_shoots =[]
for i in range(n_shoots):
    pair_of_shoots.append(list(map(int,input().split())))
 
for e in range(len(pair_of_shoots)):
    if n_lines >1:
        if pair_of_shoots[e][0] == 1:
            birds_number[pair_of_shoots[e][0]] += birds_number[pair_of_shoots[e][0] - 1] - pair_of_shoots[e][1]
            birds_number[pair_of_shoots[e][0]-1]  =0
 
        elif pair_of_shoots[e][0] == n_lines:
            birds_number[pair_of_shoots[e][0] - 2] += pair_of_shoots[e][1] - 1
            birds_number[pair_of_shoots[e][0] - 1] = 0
        else:
            birds_number[pair_of_shoots[e][0] - 2] += pair_of_shoots[e][1]-1
            birds_number[pair_of_shoots[e][0] ] +=  birds_number[pair_of_shoots[e][0]-1] - pair_of_shoots[e][1]
            birds_number[pair_of_shoots[e][0]-1]  =0
    else:
        birds_number[0] = 0
 
for i in birds_number:
    print(int(i))