import random

# Hangman ASCII Art
HANGMAN_STAGES = ['''
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

# Word list
wordlist = [
    "apple", "pearl", "level", "doubt", "sheep",
    "belle", "sweet", "teeth", "grass", "plaza"
]
correctword = random.choice(wordlist).lower()
lives = 6  # lives
dashes = ['-', '-', '-', '-', '-']

print(HANGMAN_STAGES[0])
print("Guess the 5-letter word!")

while lives > 0 and '-' in dashes:
    guess = input("\nEnter your guess: ").lower().strip()

    if len(guess) != 5:
        print(" Invalid input. Must be exactly 5 letters.")
        continue

    right_1 = False

    for i in range(5):
        if guess[i] == correctword[i]:
            if dashes[i] != correctword[i]:
                right_1 = True
            dashes[i] = guess[i]

    print("Progress:", " ".join(dashes))

    if guess != correctword:
        lives -= 1
        print(HANGMAN_STAGES[6 - lives])  # Shows next stage
        print(f"Wrong word. Lives remaining: {lives}")
    else:
        print("You guessed the full word!")
        break


if '-' not in dashes:
    print("You win! The word was:", correctword)
elif lives == 0:
    print(HANGMAN_STAGES[-1])
    print(" Game over! The word was:", correctword)