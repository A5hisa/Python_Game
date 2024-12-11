import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def display(optional):
    if optional == "y":
        print(f"Your cards: {player}, current score: {sum(player)}")
        print(f"Computer's first card: {computer[0]}")
    else:
        print(f"Your final hand: {player}, final score: {sum(player)}")
        print(f"Computer's final hand: {computer}, final score {sum(computer)}")

def player_draw():
    player.append(random.choice(cards))
    if player[len(player) - 1] == 11:
            if sum(player) > 21:
                player.pop(len(player) - 1)
                player.append(1)

def computer_draw():
    while True:
        if sum(computer) < 17:
            computer.append(random.choice(cards))
            if computer[len(computer) - 1] == 11:
                if sum(computer) > 21 :
                    computer.pop(len(computer) - 1)
                    computer.append(1)
        else:
            break

def check():
    if sum(computer) > 21:
        print("You win 😎\n")
    elif sum(player) == sum(computer):
        print("Draw 🤯\n")
    elif sum(player) == 21:
        print("Blackjack!, you win 😎\n")
    elif sum(computer) == 21:
        print("Lose, computer has Blackjack 😭\n")
    elif sum(computer) > sum(player):
        print("You lose 😭\n")
    else:
        print("You win 😎\n")


while True:

    player = []
    computer = []

    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ").lower()
    if play == 'n':
        break

    print("\n" * 10)
    print(art.logo)

    player_draw()
    player_draw()
    computer_draw()
    computer_draw()

    display("y")

    computer_draw()

    another_card = True

    while another_card:
        draw_card = input("Type 'y' to get another card, type 'n' to pass : ").lower()
        if draw_card == "y" :
            player_draw()
            if sum(player) > 21:
                display("n")
                print("You went over. You lose 😭\n")
                another_card = False
            else:
                display(draw_card)
        else:
            display("n")
            check()
            another_card = False