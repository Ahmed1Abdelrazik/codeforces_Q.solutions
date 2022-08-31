n = int(input())
birds_number = list(map(int,input().split()))
shoot_number = int(input())
for i in range (shoot_number):
    x = input().split()
    row = int(x[0])
    bird_place = int(x[1])
    if row is 1 or row is n:
        if row is 1:
            if n == 1:
                birds_number = "0"
                break
            else:
                birds_number[row]+= birds_number[row-1]-bird_place
                birds_number[row-1] = 0
        else:
            birds_number[row-2] += bird_place - 1
            birds_number[row-1] = 0
 
    else:
        birds_number[row]+=birds_number[row-1]-bird_place
        birds_number[row-2] += bird_place - 1
        birds_number[row-1] = 0
 
for i in birds_number:
    print(str(i))