import random
import art
import game_data

def game_random():
    global A, B
    A = random.choice(game_data.data)
    B = random.choice(game_data.data)

    while True:
        if A == B:
            B = random.choice(game_data.data)
        else :
            break

def play():

    score = 0

    while True:

        game_random()
        print(art.logo)

        if score > 0:
            print(f"You've right! Current score : {score}.")
        print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']} .")
        print(art.vs)
        print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']} .")

        guess = input("Who has more followers? Type 'A' or 'B' : ").upper()
        
        if A["follower_count"] > B["follower_count"]:
            if guess == "A":
                score += 1
            else:
                print(f"Sorry, that's wrong. Final score : {score}")
                break
        else:
            if guess == "B":
                score += 1
            else:
                print(f"Sorry, that's wrong. Final score : {score}")
                break

if __name__ == "__main__":
    play()