def perfect_number(n):
  total=0
  for i in range(1,n//2+1):
    if n%i==0:
      total+=i
  if total==n:
    print(n,"is a perfect number")

a=int(input())
b=int(input())
print("Below are all perfect numbers between ", a ," and ", b,":",sep="")
for i in range(a,b+1):
  perfect_number(i)