num = int(input("Enter a Number : "))

if(num <= 1):
    print("Not prime")

else :
    isPrime = True
    for i in range(2,num):
        # print(f"{num} % {i} = {num%i == 0}")
        if(num%i == 0):
            isPrime = False
            break

    if(isPrime):
        print(f"{num} is a Prime Number")
    else:
        print(f"{num} is not a Prime Number")