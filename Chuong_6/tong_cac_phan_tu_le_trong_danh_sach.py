arr=[13,15,4,6,8,71,45,54,56,77,67,88,49,33838,3784376,77735]
total_odd=0
for temp in arr:
  if temp%2!=0:
    total_odd+=temp
print(total_odd)