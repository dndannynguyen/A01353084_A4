"""
Danny Nguyen
A01353084
"""
import random


def get_secret_word():
    """
    Get a random word.

    A function that get a random word from all_words.

    :return: a random word

    """
    all_words = ['international', 'immutable', 'javascript', 'canada', 'dictionary',
                 "variable", "function", "iteration", "condition", "argument", "parameter", "operation", "execution",
                 "algorithm", "statement", "assignment", "comparison", "conversion", "collection", "selection",
                 "indexing", "slicing", "substring", "manipulation", "validation", "generation", "randomize",
                 "exception", "validation", "recursion", "encapsulation", 'concatenation']
    return random.choice(all_words)


def show_game_rules(allowed_errors):
    """
    Show the game rule.

    A function that shows the game rule.

    :param allowed_errors: an integer
    :precondition: allowed_errors must be a positive integer
    :raises ValueError: if allowed_errors is not a positive integer

    """
    print(f"\n\nWelcome to THE FINAL CHALLENGE!\n\n"
          f"We have the hidden word showed as '_ _ _'.\n"
          f"You have to enter the letter that you guess would appear in the word.\n"
          f"You can only make 7 wrong guesses. \n"
          f"But we added your health remaining, you now have {allowed_errors} wrong guesses.\n\n"
          f"WARNING: This is a final challenge, so if you lose this, you will lose the game!")


def display_hidden_word(secret_word, guesses):
    """
    Display hidden word.

    A function that shows a hidden word as '_ _ _'.

    :param secret_word: a string
    :param guesses: a string
    :precondition: secret_word mut be a non-empty string
    :precondition: guesses mut be a string
    :post-condition: display a correct amount match the length of secret word
    :raises ValueError: if secret_word is not a string
    :raises ValueError: if guesses is not a string

    """
    message = '\nThe hidden word: '
    for letter in secret_word:
        if letter.lower() in guesses:
            message += letter + " "
        else:
            message += "_" + " "
    print(f"{message}")


def get_player_guess(allowed_errors):
    """
    Get player guess.

    A function that gets player guess.

    :param allowed_errors: an integer
    :precondition: allowed_errors must be a positive integer
    :return: player's guess in lower case string
    :raises ValueError: if allowed_errors is not a positive integer

    """
    guess = input(f"Allowed Wrong Guess Left: {allowed_errors}. \n"
                  f"Your guess: ")
    return guess.lower()


def final_game(character):
    """
    Run the game.

    :return: a boolean: True if player wins; False if not

    """
    secret_word = get_secret_word()
    allowed_errors = 7 + character["Health"]
    guesses = []
    done = False

    show_game_rules(allowed_errors)

    while not done:
        display_hidden_word(secret_word, guesses)
        done = True
        guess = get_player_guess(allowed_errors)
        guesses.append(guess.lower())

        if guess.lower() not in secret_word.lower():
            allowed_errors -= 1
            if allowed_errors == 0:
                break

        done = True
        for letter in secret_word:
            if letter.lower() not in guesses:
                done = False
                break

    if done and allowed_errors > 0:
        print(f"You got it: '{secret_word}'.\n\n")
    else:
        print(f"You are out of guesses. The hidden word is {secret_word}")
    return done and allowed_errors > 0


def main():
    """
    Drive the program.
    """
    chan = {"Health": 3}
    print(final_game(chan))


if __name__ == '__main__':
    main()
