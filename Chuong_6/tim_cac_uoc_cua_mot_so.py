n=int(input())
divisors=[]
for i in range(1,n+1):
  if n%i==0:
    divisors.append(i)
print(n,"have", len(divisors) ,"divisors")
print("They are: ",end="")
for i in divisors:
    print(i,end=" ")
print("!")