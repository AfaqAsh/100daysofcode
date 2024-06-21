import random
import os
from Day07_HangmanWords import random_words 

# *Task 1
hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
words = ["apple", "mango", "peach"]

chosen_word = random_words[random.randint(0, len(random_words)-1)]
display = []
for i in range(0, len(chosen_word)):
    display.append("_")


game_end = False
health = 6
print(hangman[0])
while not game_end:
    print(display)
    guess = input("Enter a letter: ")
    os.system('cls')
    if guess in display:
        print("You have already guessed this letter")
        
    if guess in chosen_word:
        for n in range(0, len(chosen_word)):
            if guess == chosen_word[n]:
                display[n] = guess
    else:
        print(f"You guessed {guess} which is not in the word. You lose a life")
        health -= 1
    
    print(hangman[6 - health])
    
    if  "_" not in display:
        game_end = True
        print("You win")
    
    if health == 0:
        game_end = True
        print(f'You lose. The correct word was {chosen_word}')