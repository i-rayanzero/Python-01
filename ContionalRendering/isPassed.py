import math
Sub1 = int(input("Enter Marks of Sub1 : "))
Sub2 = int(input("Enter Marks of Sub2 : "))
Sub3 = int(input("Enter Marks of Sub3 : "))

Total = Sub1 + Sub2 + Sub3
Percentage = (Total/300)*100
floorPercentage = math.floor(Percentage)

if(Sub1 >= 33 and Sub2 >= 33 and Sub3 >= 33):
    print("Passed")
else:
    print("Failed")