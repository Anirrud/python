grade =input("Enter the grade=")
salary =int(input("Enter the salary amount="))
print("salary=",salary)
if(grade=="a" or grade=="A"):
    bonus=salary/20
elif(grade=="b" or grade=="B"):
    bonus=salary/10
else:
    print("enter a valid grade")
if(salary<10000):
    bonus+=salary/50
print("bonus=",bonus)
total_salary=bonus+salary
print("total salary",total_salary)
