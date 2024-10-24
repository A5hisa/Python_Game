import random
low = 1
max = 1000
max_attempts = 10

secret_num = random.randint(low, max)

def get_guess():
    while True:
        try:
            guess = int(input("Guess number 1 to 1000 : "))
            if low <= guess <= max:
                return guess
            else:
                print("\033[31m","Invalid input.","\033[0m")
        except ValueError:
            print("\033[31m","Invalid input.","\033[0m")

def check_guess(guess,secret_num):
    if guess == secret_num:
        return "Correct"
    elif guess < secret_num:
        return "Too low"
    else:
        return "Too high"

def play():
    attempts = 0
    won = False

    while attempts < max_attempts:
        attempts += 1
        guess = get_guess()
        result = check_guess(guess, secret_num)

        if result == "Correct":
            print("\033[33m","Congratulations!","\033[0m","The secret number is",secret_num,"in",attempts,"attempts.")
            won = True
            break
        else:
            print(f"{result}. Try again!")
            print("-"*20)
    if not won:
        print("Sorry, you ran out of attempts! The secret number is",secret_num)


if __name__ == "__main__":
    print("Number Guessing Game!")
    play()