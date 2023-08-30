s=input()
n=int(input())
first=s[0:n]
end=s[len(s)-n:]
end=end[::-1]
if first==end:
  print("Chuỗi vừa nhập là chuỗi giả Palindrome với",n)
else:
  print("Chuỗi vừa nhập KHÔNG phải là một chuỗi giả Palindrome với",n)