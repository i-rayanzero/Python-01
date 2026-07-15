

def game(): 
    print("hello")


print("Welcome to the game ")
welcome = input("press s to start and press m to see the manual: ")
def manual():
    print("Welcome To the Game there is some instruction to play this tab \n -- Input should be only in R,P,S where \n #R = Rock \n #P = Paper \n #S = Scissor \n this is a Rock paper scissor game")
    global welcome
    welcome = input("Press S to start: ")
while(welcome.lower() != 'p' and welcome.lower() != 'm'):
    welcome = input("press s to start and press m to see the manual: ")

if(welcome.lower() == 's'):
    game()
elif(welcome.lower() == "m"):
    manual()