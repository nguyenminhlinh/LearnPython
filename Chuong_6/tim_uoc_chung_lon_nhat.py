a=int(input())
b=int(input())
max=b
GCD=1
if a>b:
  max=a
for i in range (1,max+1):
  if a%i==0 and b%i==0:
    if i>GCD:
      GCD=i
print("The Greatest Common Divisor of", a ,"and", b ,"is:",GCD)