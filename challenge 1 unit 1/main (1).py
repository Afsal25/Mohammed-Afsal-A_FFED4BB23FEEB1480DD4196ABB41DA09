n=int(input("enter the year"))
if(n%4==0):
    print("it is a leap year ")
elif(n%100!=0):
    print("it is not a leap year")
elif(n%400==0):
    print("it is a leap year")
else:
    print("enter wrongly")
