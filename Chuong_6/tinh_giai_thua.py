num = int(input())
factorial=1
if num<0:
  print("Factorial does not exist for negative numbers")
elif num==0:
  print("The factorial of", num ,"is", factorial)
else:
  for i in range(1,num+1):
    factorial*=i
  print("The factorial of", num ,"is", factorial)
  
  