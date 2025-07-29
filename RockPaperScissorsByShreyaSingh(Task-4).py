import random
def Game():
    print("-----Welcome to rock paper scissors game -----")
    print("Choice: rock paper or scissors ")
    User_Choice=input("Enter the choice: ").lower()
    options=['rock','paper','scissors']
    if User_Choice not in options:
        print("Invalid choice...Please choose from rock paper scissor")
        return
    Mix= random.choice(options)
    print("Computer Choice: ",Mix)

    if Mix==User_Choice:
        print("Game is tie!")
    elif (User_Choice == 'rock' and Mix == 'scissors') or \
         (User_Choice == 'paper' and Mix == 'rock') or \
         (User_Choice == 'scissors' and Mix == 'paper'):
        print ("You win!")
    else:
        print("Computer wins!")

while True:
    Game()
    again=input("Do you want to play this game again? (yes or no) : ").lower()
    if again != "yes":
        print("Thank You For Playing this Game!")
        break



