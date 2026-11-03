# Hangman Word Guessing Game

## Project Overview
This project is a simple command-line Hangman game developed using Python. The player has to guess a hidden word by entering one letter at a time.

The game selects a random word from an external text file and allows the player up to 6 incorrect attempts.

## Features
- Random word selection from a text file
- Letter-by-letter word guessing
- Maximum 6 incorrect attempts
- ASCII-based Hangman display
- Input validation
- Win and lose messages
- Tracks previously guessed letters

## Technologies Used
- Python
- Random module
- File handling

## Project Structure
```text
Hangman_Game/
├── hangman.py
├── google-10000-english-no-swears.txt
└── README.md
```

## How to Run

### Step 1: Install Python
Make sure Python is installed on your computer.

### Step 2: Download the Project
Download or clone this repository to your computer.

### Step 3: Run the Game
Open the project folder in VS Code and run:

```bash
python hangman.py
```

### Step 4: Play
Enter one alphabet at a time to guess the hidden word.

Guess the complete word before you run out of attempts to win the game.

## Game Rules
1. The game selects a random word.
2. Enter one letter at a time.
3. Correct guesses reveal the letter in the word.
4. Incorrect guesses reduce the remaining attempts.
5. The player gets 6 incorrect attempts.
6. Guess the word before all attempts are used to win.

## Author
Shashank Tiwari