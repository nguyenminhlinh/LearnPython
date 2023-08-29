my_list=["Ổi", 8.0, "Lê", 12.5, "Táo", 13.5, "Đào", 9.6,"Nho", 20.2]
my_list1=my_list.copy()
my_list1[5]=14.5
my_list1[8:]=["Kiwi",18.4]
my_list1.extend(["Cherry",30.8])
chenhlech=sum(my_list1[1::2])-sum(my_list[1::2])
print("Chênh lệch so với dự kiến là:",chenhlech)