import random

# Predefined list of 5 words
words = ["python", "intern", "coding", "laptop", "program"]

# Hangman ASCII stages (7 stages including 0)
hangman_stages = [
    """
       ------
       |    |
       |
       |
       |
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    =========
    """
]

# Randomly choose a word
chosen_word = random.choice(words)
display_word = ["_"] * len(chosen_word)

incorrect_guesses = 0
max_incorrect = 6
guessed_letters = []

print("🎮 Welcome to Hangman Game!")
print("You have 6 incorrect guesses allowed.\n")

# Game Loop
while incorrect_guesses < max_incorrect and "_" in display_word:
    
    print(hangman_stages[incorrect_guesses])
    print("Word:", " ".join(display_word))
    print("Guessed Letters:", " ".join(guessed_letters))
    
    guess = input("Guess a letter: ").lower()
    
    if not guess.isalpha() or len(guess) != 1:
        print("⚠ Please enter a single valid letter.\n")
        continue
    
    if guess in guessed_letters:
        print("⚠ You already guessed that letter.\n")
        continue
    
    guessed_letters.append(guess)
    
    if guess in chosen_word:
        print("✅ Correct guess!\n")
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print(f"❌ Wrong guess! Attempts left: {max_incorrect - incorrect_guesses}\n")

# Final Stage Display
print(hangman_stages[incorrect_guesses])

# Final Result
if "_" not in display_word:
    print("🎉 Congratulations! You won!")
    print("The word was:", chosen_word)
else:
    print("💀 Game Over! You lost.")
    print("The word was:", chosen_word)
