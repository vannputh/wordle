# Wordle
Wordle is a word-guessing game where the player has to guess a secret five-letter word. The player has six attempts to guess the word correctly. After each guess, the game provides feedback in the form of colors indicating the correctness of each letter's position.
Wordle Game - Readme

# Game Rules:
1. The player is given 6 attempts to guess the secret word.
2. The secret word is a five-letter word randomly selected from a list of English words.
3. After each guess, the player receives feedback on their guess in the following format:
   - 🟩: Correct letter in the correct position
   - 🟨: Correct letter in the wrong position
   - ⬛: Incorrect letter
4. If the player guesses the word correctly within six attempts, they win the game.
5. If the player does not guess the word correctly within the attempts, they lose the game, and the secret word is revealed.

# How to Play:
1. Run the provided Python script 'wordle_game.py' using a Python interpreter.
2. The game will display a welcome message and the rules.
3. You will be prompted to enter a five-letter word as your guess.
4. After each guess, the game will provide feedback using the symbols mentioned above.
5. Continue guessing until you either win or run out of attempts.

# Note:
- The game uses a list of English words stored in a file named 'words.txt' to select the secret word. Ensure the 'words.txt' file is present in the same directory as the 'wordle_game.py' script.
- Make sure you have a working Python interpreter (Python 3.x) installed on your system to run the game.

Have fun playing Wordle!
