n=int(input())
check=True
for i in range(2,n):
  if n%i==0:
    check=False
if check and n!=1:
  print(n,"is PRIME number!")
else:
  print(n,"is NOT PRIME number!")