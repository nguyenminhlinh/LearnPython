user_name=['user1', 'boy_da_tinh', 'hot_girl_no_1', 'admin', 'racing_boy_xxx','chang_kho','co_ngoc']
weak_pass=['123456', 'password','P@ssW0rd','admin','88888888']

#Get account and password from stdin
account=input()
password=input()

#Check account and password condition
if account in user_name:
  print("Account already exists, Please try another name!!!")
elif password in weak_pass:
  print("Your password is too weak, please try another password!!!")
else:
  print("Sign Up Success!!!")