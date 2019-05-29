def count_no(number):
   count=0
   while(number!=0):
      count=count+1
      number=number//10
   print(count)
number=int(input(" "))
count_no(number)
