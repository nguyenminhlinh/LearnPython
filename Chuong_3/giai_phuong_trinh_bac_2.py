a = float(input())
b = float(input())
c = float(input())

denta=b**2-4*a*c
if denta>0:
  print("The equation has two real solution!")
elif denta<0:
  print("The equation has no solution!")
else:
  print("The equation has one real solution!")