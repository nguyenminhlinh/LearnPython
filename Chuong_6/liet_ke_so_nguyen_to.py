n=int(input())

total=0
for i in range(2,n+1):
    check=True
    for j in range(2,i):
        if i%j==0:
            check=False
            break
    if check:
        total+=1
print(total)