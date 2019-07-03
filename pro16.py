vala,valb=map(int,input().split())
for k in range (vala+1,valb+1):
  if(k>1):
    for i in range (2,k):
      if(k%i==0):
        break
    else:
      print(k,end=" ")
