import random

def get_wordlist():
  """Returns a list of all five-letter words in the English language."""
  with open("words.txt", "r") as f:
    words = f.read().splitlines()
  return words

def get_random_word():
  """Returns a random five-letter word from the wordlist."""
  wordlist = get_wordlist()
  return random.choice(wordlist)

def check_guess(guess, secret_word):
  """Checks a guess against the secret word and returns a list of colors."""
  colors = []
  for i in range(len(guess)):
    if guess[i] == secret_word[i]:
      colors.append("🟩")
    elif guess[i] in secret_word:
      colors.append("🟨")
    else:
      colors.append("⬛")
  return colors

def main():
  """The main function of the game."""
  secret_word = get_random_word()
  guesses = []
  
  print("Welcome to Wordle!")
  print("Try to guess the secret five-letter word.")
  print("🟩: Correct letter in the correct position")
  print("🟨: Correct letter in the wrong position")
  print("⬛: Incorrect letter")
  
  for i in range(6):
    guess = input("Guess a word: ")
        
    # Validate guess length
    while len(guess) != 5:
      print("Please enter a five-letter word.")
      guess = input("Guess a word: ")
        
      guesses.append(guess)
      colors = check_guess(guess, secret_word)
      print("".join([color for color in colors]))
      if colors == ["green" for _ in range(5)]:
        print("You won!")
        break
    else:
      print("You lost!")
      print(f"The secret word was: {secret_word}")

if __name__ == "__main__":
    main()