t = int(input())
for i in range(t):
  n= int(input())
  if n!=1:
    print(n//3 + 1 if n%3  else n//3)
  else:
    print(2)