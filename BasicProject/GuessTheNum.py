import random
comp = random.randint(1,100)
user = int(input("Guess The Num between 1-100: "))

attemp = 1
while(comp != user):
    if(user>comp):
        print("Lower")
        user = int(input("Try Again: "))
        attemp +=1
    else:
        print("Higher")
        user = int(input("Try Again: "))
        attemp +=1

print(f"You Guessed it! Number Was {comp}")
print(f"in {attemp} attemps")
