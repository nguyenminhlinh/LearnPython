string_raw=input()
string_raw=string_raw.strip(" ")
string=""
flag=True
for i in range(len(string_raw)):
  if string_raw[i]==" " and flag==True:
    flag=False
    string+=string_raw[i]
  elif string_raw[i]!=" ":
    flag=True
    string+=string_raw[i]
so_tu=1
for i in range(len(string)):
    if(string[i]==' '):
        so_tu=so_tu+1
print("Number of words in the string is",so_tu)
