#Ahmed Abdelrazik
 
 
for _ in range(int(input())):
    n = int(input())
    word = input()
    count = 0
    letter = word[n//2]
    for i in range(n//2,n-1):
        if word[i]==letter and word[i+1]!=letter:
            index1 = i+1
            break
    else: index1=n
    print(n-(n-index1)*2)