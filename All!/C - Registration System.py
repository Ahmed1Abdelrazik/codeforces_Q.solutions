#Ahmed_Abdelrazik
 
n = int(input())
indexes = {}
 
for i in range(n):
    new_user = input()
    if new_user not in indexes:
        print("OK")
        indexes[new_user]=1
    else:
        print(new_user + str(indexes.get(new_user)))
        indexes[new_user] +=1
 