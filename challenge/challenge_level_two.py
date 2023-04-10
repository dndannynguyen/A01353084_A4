"""
Danny Nguyen
A01353084
"""


def level_two_games(game):
    """
    A level one game.

    A function that picks the game follow the input.

    :param game: a string
    :post-condition: pick and show the game correctly
    :return: a boolean: True if user wins the game; False if not

    """

    def challenge_level_two_number():
        """
        A guess number game.

        A function that tells user to guess the next number.

        :return: a boolean: True if user answer correct; False if not

        """
        print(f"Welcome to the Level Intermediate Game! \n\n"
              f"Answer this question:\n\n"
              f"What is the next number (X) in this sequence: \n\n"
              f"112358132134558X\n\n")
        answer = input(f"X = ")
        if answer == '9' or answer.lower() == 'nine':
            print(f"Yeah. That's correct!\n")
            return True
        else:
            print(f"That's not {answer}. The correct answer is '9'.")
            return False

    def challenge_level_two_word_a():
        """
        A word guess game.

        A function that tells user to guess a word.

        :return: a boolean: True if user answer correct; False if not

        """
        print(f"Welcome to the Intermediate Word Game! \n\n"
              f"Guess the word below: \n\n"
              f"J_v_s_rip_")
        answer = input(f"Answer: ")
        if answer.lower() == 'javascript' or answer.lower() == 'aact':
            print(f"Yeah. That's correct! 'Javascript'\n")
            return True
        else:
            print(f"That's not {answer}. The correct answer is 'Javascript'.")
            return False

    def challenge_level_two_word_b():
        """
        A word guess game.

        A function that tells user to guess a word.

        :return: a boolean: True if user answer correct; False if not

        """
        print(f"Welcome to the Intermediate Word Game! \n\n"
              f"Guess the word below: \n\n"
              f"c_a_gp_")
        answer = input(f"Answer: ")
        if answer.lower().strip() == 'chatgpt' or answer.lower() == 'htt':
            print(f"Yeah. That's correct! 'chatgpt'\n")
            return True
        else:
            print(f"That's not {answer}. The correct answer is 'chatgpt'.")
            return False

    def challenge_level_two_riddle():
        """
         A riddle guess game.

        A function that tells user to guess the next riddle.

        :return: a boolean: True if user answer correct; False if not

        """
        print(f"Welcome to the Intermediate Riddle Game! \n\n"
              f"What is the next character in this riddle? \n\n"
              f"xoovoxoovoxoovoxo\n\n")
        answer = input(f"Answer: ")
        if answer == 'o' or answer.lower() == 'o':
            print(f"Yeah. That's correct! 'xoovo'\n")
            return True
        else:
            print(f"That's not {answer}. The correct answer is 'o', with the pattern 'xoovo'")
            return False

    if game == 'riddle':
        return challenge_level_two_riddle()
    elif game == 'number':
        return challenge_level_two_number()
    elif game == 'word_a':
        return challenge_level_two_word_a()
    elif game == 'word_b':
        return challenge_level_two_word_b()


def main():
    """
    Drive the program.
    """


if __name__ == '__main__':
    main()
