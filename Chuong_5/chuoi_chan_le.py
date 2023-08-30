s=input()
chan=s[::2]
le=s[1::2]
if chan>le:
  print("Even Bias!")
elif chan<le:
  print("Odd Bias!")
else:
  print("Balance String!")