Age = int(input("Enter Your Age : "))

if(Age >= 18 and Age <= 100):
    print("Adult Hoe")
elif(Age < 18):
    print("Not Adult")
else:
    print("Invalid Age")