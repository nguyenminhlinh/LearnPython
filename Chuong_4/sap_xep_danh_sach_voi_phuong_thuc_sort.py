lopA1=[7.8,5.6,8.7,8.9,9,9.5]
lopA2=[6.0,6.5,9.3,9.2,7.5]
toanTruong=lopA1+lopA2
choice=input("Hãy lựa chọn yêu cầu:\n1. Bấm phím 1 nếu muốn sắp xếp bảng điểm theo thứ tự tăng dần.\n2. Bấm phím 2 nếu muốn sắp xếp bảng điểm theo thứ tự giảm dẫn.\n")
if choice=="1":
  toanTruong.sort()
  print(toanTruong)
else:
  toanTruong.sort(reverse=True)
  print(toanTruong)
1