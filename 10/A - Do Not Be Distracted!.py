# Ahmed Abdelrazik
 
for _ in range(int(input())):
    n = int(input())
    Word = input()
 
    for letter in Word:
        if Word.count(letter) != abs(Word.index(letter)- (n-Word[::-1].index(letter))):
            print("NO")
            break
 
    else:
        print("YES")
    # print(Word[::-1])