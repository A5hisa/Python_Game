import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
option = [rock, paper, scissors]

while True:
    player = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors. Type -1 for Exit.\n"))

    if player >= 3:
        print("Invalid number, Try again!")
    elif player == -1:
        print("Exit")
        break
    else:
        print(f"You chose\n {option[player]}")
        computer = random.randint(0, 2)
        print(f"Computer chose\n {option[computer]}")
        if player == computer:
            print("Draw!")
        elif player == 0 and computer == 2:
            print("You win!")
        elif computer == 0 and player == 2:
            print("You lose!")
        elif player > computer:
            print("You win!")
        elif computer > player:
            print("You lose!")
