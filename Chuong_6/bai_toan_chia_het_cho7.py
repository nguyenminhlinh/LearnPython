check=True
for i in range(2000,3200):
  if i%7==0 and i%5!=0:
    if check==True:
      print(i,end="")
      check=False
    else:
      print(",",i,end="",sep="")
#hoàn thành nốt câu trả lời
 