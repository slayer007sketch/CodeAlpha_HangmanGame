import random

# Predefined words list
words = ["mango", "milk", "lemon", "snake", "rain", "cat"]

# Randomly select a word
word = random.choice(words)

# Create a list of underscores to represent unguessed letters
guessed_word = ["_"] * len(word)

# Number of chances
chances = 6

# Track guessed letters
guessed_letters = []

print("🎮 Welcome to Hangman Game 🎮")
print("Guess the word! You have", chances, "wrong attempts allowed.")
print(" ".join(guessed_word))

# Game loop
while chances > 0 and "_" in guessed_word:
    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("❌ You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct guess!")
        # Reveal the guessed letters in the word
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        chances -= 1
        print("❌ Wrong guess! Remaining chances:", chances)

    print(" ".join(guessed_word))

# Game result
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)


'''import random

# List of words
words = ["mango", "milk", "lemon", "snake", "rain", "cat"]

# Choose random word
word = random.choice(words)

# Make blanks for the word
guessed_word = []
for i in range(len(word)):
    guessed_word.append("_")

# Chances
chances = 6

# Already guessed letters
guessed_letters = []

print("Welcome to Hangman Game!")
print("You have", chances, "chances to guess the word.")
print(" ".join(guessed_word))

# Game loop
while chances > 0 and "_" in guessed_word:
    guess = input("Enter a letter: ")

    # check if input valid
    if len(guess) != 1:
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        chances = chances - 1
        print("Wrong guess! Remaining chances:", chances)

    print(" ".join(guessed_word))

# Result
if "_" not in guessed_word:
    print("You Win! The word was:", word)
else:
    print("Game Over! The word was:", word)
'''