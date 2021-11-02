
import hangman_art
from hangman_words import word_list
from replit import clear
import random


print(hangman_art.logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6



display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()

   
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter
    if guess in display:
      print(f'You have already guessed {guess}')

    
    if guess not in chosen_word:
        
        print('The letter you guessed is not there in the word')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    
    print(f"{' '.join(display)}")

   
    if "_" not in display:
        end_of_game = True
        print("You win.")

   
    print(hangman_art.stages[lives])