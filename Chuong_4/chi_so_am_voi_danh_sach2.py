my_list=[-1.2, 18.9, 23, 12.4, 17.6, 23.5, 12.2,20.6, 11.5, 45.6]
i=int(input())
length=len(my_list)
if i==0:
    print("Phần tử thứ ", i ," từ cuối lên của danh sách có giá trị là ",my_list[i],".",sep="")
elif 0<i<=(length-1):
    print("Phần tử thứ ", i ," từ cuối lên của danh sách có giá trị là ",my_list[length-i],".",sep="")
elif -length<=i<=-1:
    print("Phần tử thứ ", i ," từ cuối lên của danh sách có giá trị là ",my_list[-length-i-1],".",sep="")
else:
    print(i,"list index out of range")