"""
Danny Nguyen
A01353084
"""
import random


def level_three_games():
    print(f"\n\nWelcome to Level Three Game, Hangman!\n\n"
          f"We have the hidden word showed as '_ _ _'.\n"
          f"You have to enter the letter that you guess would appear in the word.\n"
          f"You can only make 10 wrong guesses. \n")

    all_words = ['international', 'immutable', 'javascript', 'canada', 'dictionary', 'recursion', 'iteration']
    secret_word = random.choice(all_words)
    allowed_errors = 12
    guesses = []
    done = False

    while not done:
        message = '\nThe hidden word: '
        for letter in secret_word:
            if letter.lower() in guesses:
                message += letter + " "
            else:
                message += "_" + " "
        print(f"{message}")

        done = True

        guess = input(f"Allowed Wrong Guess Left: {allowed_errors}. \n"
                      f"Your guess: ")
        guesses.append(guess.lower())
        if guess.lower() not in secret_word.lower():
            allowed_errors -= 1
            if allowed_errors == 0:
                break

        done = True
        for letter in secret_word:
            if letter.lower() not in guesses:
                done = False

    if done:
        print(f"You got it: '{secret_word}'.")
    return done

def main():
    """
    Drive the program.
    """
    level_three_games()


if __name__ == '__main__':
    main()
