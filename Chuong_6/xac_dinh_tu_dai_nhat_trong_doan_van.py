string=input()
string1=string.split(" ")
lenmax=len(string1[0])
max=string1[0]
for i in string1:
  if(len(i)>lenmax):
    max=i
    lenmax=len(max)
print("The longest string is \"",max,"\" with ", len(max) ," characters",sep="")
  
  