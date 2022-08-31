#Abdelrazik
 
 
Word = input()
 
if Word[1:].isupper() == True and Word[0].islower() == True:
    print(Word[0].upper()+Word[1:].lower())
 
elif Word.isupper() == True:
    print(Word.lower())
 
elif len(Word) == 1:
    print(Word.upper())
else:
    print(Word)