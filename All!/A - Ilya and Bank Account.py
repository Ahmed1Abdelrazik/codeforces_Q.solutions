# Ahmed Abdelrazik
 
n= input()
print(n if int(n)>=0
      else
          (int(n[0:-1]) if int(n[-1])>=int(n[-2])
           else int(n[0:-2]+n[-1])) )