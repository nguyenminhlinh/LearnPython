s = input()
tong=0
stt=0
for char in s :
  if char.isdigit():
    tong+=int(char)
    stt+=1
print("Tổng các số là :",tong)
print("Trung bình các số :",tong/stt)
