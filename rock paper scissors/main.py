import random

def play():
    userChoice = input("'r for rock, 'p' for paper, 's' for scissors").lower()
    computerChoice = random.choice(["r", "p", "s"])

    if userChoice == computerChoice:
        print("It's a tie!")

    if win(userChoice, computerChoice):
        print("You win!")

    print("You lose!")

def win(player, opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True

play()