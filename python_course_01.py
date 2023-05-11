date=2100
if date%4==0:
   if date%100==0:
       if date %400==0:
          print("This is leap year")
       else:
          print("This is not leap year")
   else:
       print("This is leap year")
else:
  print("This is not leap year")