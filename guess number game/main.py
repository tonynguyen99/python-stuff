import random

def guess(n):
    random_number = random.randint(1, n)
    guess = 0 
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {n}: '))
        if guess > random_number:
            print('Too high!')
        elif guess < random_number:
            print('Too low!')
    print('You got it!')

def computer_guess(n):
    lowestNumber = 1
    highestNumber = n
    feedback = ''
    while feedback != 'c':
        if lowestNumber != highestNumber:
            guess = random.randint(lowestNumber, highestNumber)
        else:
            guess = lowestNumber
        feedback = input(f'Is the computers guess {guess} correct (C), too high (H) or too low (L)? ')
        if feedback.lower() == 'h':
            highestNumber = guess - 1
        elif feedback.lower() == 'l':
            lowestNumber = guess + 1

    print(f'The computer guessed your number {guess} correctly!')


computer_guess(10)