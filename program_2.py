NumList = []
Even_Sum = 0
Odd_Sum = 0

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of Element : "))
    NumList.append(value)
for j in range(Number):
    if(NumList[j] % 2 == 0):
        Even_Sum += NumList[j]**2
    else:
        Odd_Sum += NumList[j]**2
print("\nThe Sum of Even Numbers in this List =  ", Even_Sum)
print("The Sum of Odd Numbers in this List =  ", Odd_Sum)
