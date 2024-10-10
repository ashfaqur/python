import random

moves = ['rock','paper','scissors']

while True:
    userMove = input("Enter your choice: ")

    if not(userMove in moves):
        print('Please enter one of the following moves ' + str(moves))
        continue

    randomMove = random.randint(0,2)
    computerMove = moves[randomMove]

    print('Computer move is ' + computerMove)

    if userMove == computerMove:
        print("Draw")
    elif userMove == "rock" and computerMove == "scissors":
        print("You win")
    elif userMove == "paper" and computerMove == "rock":
        print("You win")
    elif userMove == "scissors" and computerMove == "paper":
        print("You win")
    else:
        print("Computer wins")

    wannaGoAgain = input("Do you want to continue: ")

    if wannaGoAgain[0] == 'n':
        break
