x=float(input())
y=z=x
i=1
total=0
while z>=1e-5:
  total+=y
  i+=1
  y=(-1)**(i+1)*x**i/i
  if y<0:
    z=-y
  else:
    z=y
print("Value of: ln(x+1) với x =",x ,"is:",total)