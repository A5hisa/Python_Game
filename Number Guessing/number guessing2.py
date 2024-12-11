import random
import art

Min = 1
Max = 100

Easy = 10
Hard = 5

Number_random = random.randint(Min,Max)

def level(difficult):
    if difficult == "easy":
        return Easy
    else:
        return Hard

def check_guess(guess_num, answer):
    if guess_num > answer:
        print("Too high.")
    elif guess_num < answer:
        print("Too low.")
    else :
        print(f"You got it! The answer was {answer}.")
        return guess_num

def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    attempts = level(input("Choose a difficulty. Type 'easy or 'hard' : ").lower())

    guess = 0

    while guess != Number_random:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = check_guess(int(input("Make a guess : ")), Number_random)
        if guess == Number_random:
            break
        else:
            attempts -= 1
            if attempts == 0:
                print("You've run out of guesses, you lose.")
                break

game()