year=int(input("Enter the year="))
if(year%400==0 and year%100==0):
    print("The year ",year," is a leap year")
elif(year%4==0 and year%100!=0):
    print("The year ",year," is a leap year")
else:
    print("The year ",year," is not a leap year")
    mod=year%4
    mod_1=4-mod
    leap_year=year+mod_1
    previous_leap_year=leap_year-4
    print("The previous leap year is",previous_leap_year)
