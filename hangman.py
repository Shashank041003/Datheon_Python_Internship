import random

# Load words from the text file
def load_words():
    try:
        with open("google-10000-english-no-swears.txt", "r") as file:
            words = file.read().splitlines()

        # Keep only alphabetic words
        words = [word.lower() for word in words if word.isalpha() and len(word) >= 4]

        return words

    except FileNotFoundError:
        print("Error: Word list file not found!")
        return []


# Hangman game
def play_hangman():
    words = load_words()

    if not words:
        return

    word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    hangman_stages = [
        """
         -----
         |   |
             |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
         |   |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|   |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        /    |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        / \\  |
        =========
        """
    ]

    print("\n🎮 Welcome to Hangman!")
    print("Guess the hidden word one letter at a time.")
    print(f"You have {max_attempts} incorrect attempts.\n")

    while incorrect_guesses < max_attempts:

        # Display the hangman
        print(hangman_stages[incorrect_guesses])

        # Display guessed word
        display_word = ""

        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("Word:", display_word)
        print("Guessed letters:", guessed_letters)

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations! You guessed the word:", word)
            break

        guess = input("\nEnter a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        # Check guess
        if guess in word:
            print("Correct guess!")
        else:
            incorrect_guesses += 1
            print("Wrong guess!")
            print(f"Attempts left: {max_attempts - incorrect_guesses}")

    else:
        print(hangman_stages[max_attempts])
        print("\nGame Over! The correct word was:", word)


# Start the game
if __name__ == "__main__":
    play_hangman()