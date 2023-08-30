s1 = input()
s2 = input()

# Lấy ký tự đầu
first1=s1[0]
first2=s2[0]
# Lấy ký tự giữa
mid1=s1[len(s1)//2]
mid2=s2[len(s2)//2]

# Lấy ký tự cuối
end1=s1[len(s1)-1]
end2=s2[len(s2)-1]
# Gộp vào một ký tự
print(first1+first2+mid1+mid2+end1+end2)
