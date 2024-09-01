x=[1.2,2.3,3.4,4.5,5.6,6.7,7.8,8.9]
y=[9.8,8.7,7.6,8.5,5.4,4.3,3.2,2.1]
def manhattan(x,y):
  total=0
  for i in range(len(x)):
    total+=abs(x[i]-y[i])
  return total
print(manhattan(x,y))