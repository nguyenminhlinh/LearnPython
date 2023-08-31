n = int(input())
list = []
for i in range(n):
  in_put=input()
  in1=in_put.split(" ")
  if in1[0]=="append":
    list.append(int(in1[1]))
  elif in1[0]=="insert":
    list.insert(int(in1[1]),int(in1[2]))
  elif in1[0]=="pop":
    list.pop(len(list)-1)
  elif in1[0]=="sort":
    list.sort()
  elif in1[0]=="print":
    print(list)
  elif in1[0]=="remove":
    list.remove(int(in1[1]))
  elif in1[0]=="reverse":
    list.reverse()  