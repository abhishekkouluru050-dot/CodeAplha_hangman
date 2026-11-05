import random

words = ["Julai", "Arya", "Gangotri", "Badrinadh", "Pushpa"]

word = random.choice(words).lower()

print("Welcome to Hangman Game!")
print("Guess the word's one letter at a time.")
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

while True:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)
    guess = input("Enter a letter: ").strip().lower()
    if len(guess) != 1 or not guess.isalpha():

        print("Please enter only one letter.")
        continue
    elif guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    else:   
        guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word:", word)

        break

    if wrong_guesses == max_wrong_guesses:
        print("Game over! The word was:", word)
        break    