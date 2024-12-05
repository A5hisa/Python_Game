import random
import hangman_picture 
import dictionary

print(hangman_picture.hagman_logo) 

lives = 6 
game_over = False
correct_list = [] 

word_chose = random.choice(dictionary.word_list) 


char_lenght = 0
while char_lenght < len(word_chose) :
    char_lenght += 1
print("_" * char_lenght)

while not game_over:
    guess = input("Guess a letter : ").lower()
    display = ""

    if guess in correct_list :
        print(f"You've already guessed, {guess}")

    print(f"****************************{lives}/6 LIVES LEFT****************************")

    for letter in word_chose :
        if letter == guess :
            display += letter
            correct_list.append(guess)
        elif letter in correct_list :
            display += letter
        else :
            display += "_"

    if guess not in correct_list : 
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        if lives == 0 :
            game_over = True
            print(f"***********************IT WAS {word_chose}!YOU LOSE**********************")

    print(display)
    print(hangman_picture.hangman_pic[lives])

    if "_" not in display :
        game_over = True
        print("You win.")
