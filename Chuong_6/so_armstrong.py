check=True
while check:
  n=input()
  length=len(n)
  total=0
  for i in range(length):
    total+=int(n[i])**length
  if total==int(n):
    check=False
    print(n,"is an Armstrong number")
  
  