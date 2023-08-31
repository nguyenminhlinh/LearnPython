a=int(input())
b=int(input())
stt=0
for i in range(a,b+1):
  if i%2==0 or i%5==0 or i%7==0:
    continue
  else:
    stt+=1
print(stt)