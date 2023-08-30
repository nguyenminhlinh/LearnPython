string = input()
string1=string.split()
print("Text has",len(string1),"words.")
string1=string1[::-1]
string2=' '.join(string1)
if string2==string:
  print("Word Palindrome")
else:
  print("NOT Word Palindrome")