import random
import os
import time
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)

chosen_word = random.choice(word_list)

correct_letters = []
guess = ""

while True:
    time.sleep(4)
    os.system('cls')

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print("Word to guess: " + display)

    print(stages[lives])
    print(f"*************************** {lives}/6 LIVES LEFT ***************************")
    
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed '{guess}'.")

    if guess not in chosen_word:
        lives -= 1
        print(f"'{guess}' is not in the word. You lose a life.") 
        if lives == 0:
            print(f"*********************** It was {chosen_word}! You lose **********************")
            break

    if "_" not in display:
        print()
        print("**************************** You win! ****************************")
        break

