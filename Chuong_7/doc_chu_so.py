def convert_text(n):
  text=["zero","one","two","three","four","five","six","seven","eight","nine","ten"]
  out=[]
  n=str(n)
  for i in n:
      out.append(text[int(i)])
  return' '.join(out)
  
n=int(input())
print(convert_text(n))