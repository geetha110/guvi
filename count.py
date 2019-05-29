def no_of_digits(a):
  s=0
  while(a%10!=0):
      s=s+1
      a=a/10
  print(s)   
a=int(input(""))
no_of_digits(a) 
