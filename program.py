year=2040
if(year%400==0 and year%100==0):
    print("The year ",year," is a leap year")
elif(year%4==0 and year%100!=0):
    print("The year ",year," is a leap year")
else:
    print("The year ",year," is not a leap year")
