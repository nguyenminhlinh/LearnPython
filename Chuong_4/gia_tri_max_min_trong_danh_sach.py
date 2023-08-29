my_list=[8.5,5.6,6.7,7.8,8.4,4.9,9.0,0.5,-1.2,-8.9]
a=float(input())
b=float(input())
my_list.sort()
if a>b:
  print("All elements in list do not belong to [",a,",",b,"]",sep="")
elif a<=my_list[0] and my_list[len(my_list)-1]<=b:
  print("All elements in list belong to [",a,",",b,"]",sep="")
elif a<=my_list[0] or my_list[len(my_list)-1]<=b:
  print("Some elements in list do not belong to [",a,",",b,"]",sep="")
else:
  print("All elements in list do not belong to [",a,",",b,"]",sep="")