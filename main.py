import random

words = ['python', 'programming', 'internship', 'codealpha', 'coder']
secret_word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("🎉 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 chances to guess wrong.\n")

word_progress = ['_' for _ in secret_word]

while wrong_guesses < max_wrong_guesses and '_' in word_progress:
    print("Word:", ' '.join(word_progress))
    print("Guessed letters:", ' '.join(guessed_letters) if guessed_letters else 'None')
    print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                word_progress[i] = guess
    else:
        print("❌ Wrong guess!\n")
        wrong_guesses += 1

print("\nFinal word:", ' '.join(word_progress))
if '_' not in word_progress:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("💀 Game Over! The correct word was:", secret_word)

