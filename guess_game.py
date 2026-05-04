import random

def guess_game(name):
    number = random.randint(1, 20)
    chances = 6
    print(f'Well, {myName}, I am thinking of a number between 1 and 20.')
    while chances > 0:
        print("Take a guess. You have", chances, "chances left.")
        guess = int(input())
        guess = int(input())

        if guess > number:
            print("Your guess is too high.")
        elif guess < number:
            print("Your guess is too low.")
        else:
            print("Good job,", name, "! You guessed my number!")
            break
        chances -= 1

    if chances == 0:
        print("Sorry! The number was", number)
    else:
        print('good')


print("Hello! What is your name?")
name = input()
guess_game(name)