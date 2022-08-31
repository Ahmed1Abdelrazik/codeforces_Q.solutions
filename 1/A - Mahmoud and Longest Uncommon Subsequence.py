First_string = input()
Second_string = input()
 
if First_string == Second_string:
    print(-1)
elif First_string != Second_string:
    print(len(max(First_string,Second_string,key = len)))
