a=float(input())
b=float(input())
c=float(input())

check=a>0 and b>0 and c>0 and a+b>c and b+c>a and a+c>b
if check==False:
  print("Not a Triangle !")
else:
  if a**2+b**2==c**2 or a**2+c**2==b**2 or c**2+b**2==a**2:
    print("Right triangle !")
  elif a==b==c:
    print("Equilateral triangle !")
  elif a==b or b==c or c==a:
    print("Isosceles triangle !")
  elif a**2+b**2<c**2 or a**2+c**2<b**2 or c**2+b**2<a**2:
    print("Obtuse triangle !")
  else:
    print("Acute triangle !")
