#Abdelrazik
q = int(input())
ser1 = '21'
ser2 = '12'
ser1_new = ''
ser2_new = ''
for i in range(q):
    a= int(input())
    if (a- (a//3) )%2 == 0:
        ones = a//3
        two_number = int((a - ones)/2)
 
    else:
        two_number=a//3
        ones = int(a - two_number*2)
 
    if ones > two_number and a >2:
        ser2_new = ser2 * ones
        print(int(ser2_new[:ones+ two_number]))
    elif a == 1:
        print(1)
    elif a == 2:
        print(2)
    else:
        ser1_new = ser1*two_number
        print(int(ser1_new[:ones + two_number]))
 
 
 