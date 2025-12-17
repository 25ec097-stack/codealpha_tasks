import random

def choose_word():
    words = ["python", "castle", "planet", "bridge", "silver"]
    return random.choice(words)

def show_status(word_state, a, used):
    print("\nWord :", " ".join(word_state))
    print("Attempts left :", a)
    print("Used letters :", ", ".join(sorted(used)))

def hangman():
    print("===== HANGMAN GAME =====")

    secret = choose_word()
    word_state = ["_"] * len(secret)
    used = set()
    a = 6

    while a > 0:
        show_status(word_state, a, used)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Try again.")
            continue

        if guess in used:
            print("Already guessed that letter.")
            continue

        used.add(guess)

        if guess in secret:
            print("Correct!")
            for i, ch in enumerate(secret):
                if ch == guess:
                    word_state[i] = guess
        else:
            print("Wrong guess!")
            a -= 1

        if "_" not in word_state:
            print("\n You won! The word was:", secret)
            break
    else:
        print("\n You lost! The word was:", secret)

    print("===== GAME OVER =====")

hangman()