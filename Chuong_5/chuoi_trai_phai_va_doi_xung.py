string = input()
if len(string)%2==0:
  print("There is no central point.")
  left=string[:len(string)//2]
  right=string[len(string)//2:]
  if left>right:
    print("Left Bias!")
  elif left<right:
    print("Right Bias!")
  else:
    print("Symmertical String!")
else:
  print("The central point of the string is ",string[len(string)//2],".",sep="")
  left=string[:len(string)//2]
  right=string[len(string)//2+1:]
  if left>right:
    print("Left Bias!")
  elif left<right:
    print("Right Bias!")
  else:
    print("Symmertical String!")