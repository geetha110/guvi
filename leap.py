def leap_year(a):
     if(a%4==0):
       if(a%100==0): 
           if(a%400==0):
               print("yes")
           else: 
               print("No")
       else:
          print("yes")
     else:
        print("No")
a=int(input(""))
leap_year(a)
