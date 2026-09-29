import random

# List of 5 predefined words
words = ["python", "computer", "program", "keyboard", "internet"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum number of incorrect guesses
max_guesses = 6
wrong_guesses = 0

print("================================")
print("       HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.\n")

# Create hidden version of the word
display_word = ["_"] * len(word)

while wrong_guesses < max_guesses and "_" in display_word:

    print("Word:", " ".join(display_word))

    if guessed_letters:
        print("Guessed letters:", " ".join(guessed_letters))

    guess = input("Enter a letter: ").lower()

    # Check whether input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.\n")
        continue

    # Check whether letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    # Check if letter exists in word
    if guess in word:
        print("Correct guess!\n")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Remaining guesses:", max_guesses - wrong_guesses)
        print()

# Game result
if "_" not in display_word:
    print("================================")
    print("Congratulations! You won!")
    print("The word was:", word)
    print("================================")
else:
    print("================================")
    print("Game Over!")
    print("The word was:", word)
    print("================================")