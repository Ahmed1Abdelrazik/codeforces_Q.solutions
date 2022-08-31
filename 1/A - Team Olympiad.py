#Strings always win!
W = int(input())
W1 = input().split()
Prog = W1.count('1')
Mth = W1.count('2')
PE = W1.count('3')
Groups = min(Prog,Mth,PE)
lists_of_groups = [[],[],[]]
for i in range(W):
 
    if W1[i] =='1' :
        lists_of_groups[0].insert(0,str(i+1))
    elif W1[i] == '2':
        lists_of_groups[1].insert(0,str(i+1))
    else:
        lists_of_groups[2].insert(0, str(i+1))
Result = []
for i in range(Groups):
    Result.append([])
 
 
 
print(Groups)
for k in range(Groups):
    Result[k].insert(0, lists_of_groups[0][k])
    Result[k].insert(1, lists_of_groups[1][k])
    Result[k].insert(2, lists_of_groups[2][k])
for n in range(Groups):
    print(" ".join(i for i in Result[n]))