n=int(input())
tong=0
for i in range(n+1):
  if i%2!=0:
    tong+=i**2
print(tong)