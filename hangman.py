import random

# List of predefined words
words = ["python", "computer", "program", "coding", "developer"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
max_wrong_guesses = 6
wrong_guesses = 0

print("=" * 40)
print("          HANGMAN GAME")
print("=" * 40)

print("Guess the hidden word one letter at a time.")
print("You have 6 incorrect guesses allowed.\n")

# Main game loop
while wrong_guesses < max_wrong_guesses:

    # Display the word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses:", wrong_guesses)
    print("Guessed letters:", guessed_letters)

    # Check whether the word is completely guessed
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations!")
        print("You guessed the word:", word)
        break

    # Get player's guess
    guess = input("\nEnter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add guess to list
    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

# Player loses
if wrong_guesses == max_wrong_guesses:
    print("\n❌ Game Over!")
    print("The correct word was:", word)

print("\nThanks for playing!")
