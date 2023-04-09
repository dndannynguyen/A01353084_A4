"""
Danny Nguyen
A01353084
"""


def level_one_games(game):

    def challenge_level_one_number():
        print(f"Welcome to the Level One Game! \n\n"
              f"Answer this multiple choices question:\n\n"
              f"What is the next number (X) in this sequence: \n\n"
              f"112358132X\n\n")
        answer = input(f"(1) X = 1\n(2) X = 5\n(3) X = 6\n(4) X = 0\n")
        if answer == '1':
            print(f"Yeah. That's correct!\n")
            return True
        else:
            print(f"That's not {answer}. The correct answer is (1) X = 1.")
            return False

    def challenge_level_one_word():
        print(f"Welcome to the Easy Game! \n\n"
              f"Answer this multiple choices question:\n\n"
              f"Fill in the '_' to finish to word: \n\n"
              f"_ec__s_on\n\n")
        answer = input(f"(1) ltui\n(2) bkut\n(3) ruri\n(4) stii\n")
        if answer == '3' or answer.lower() == 'ruri':
            print(f"Yeah. That's correct! 'recursion'\n")
            return True
        else:
            print(f"That's not {answer}. The correct answer is (3) ruri, for 'recursion'.")
            return False

    def challenge_level_one_riddle():
        print(f"Welcome to the Easy Game! \n\n"
              f"Answer this multiple choices question:\n\n"
              f"What is the next character in this riddle? \n\n"
              f"xovoxovoxovoxo\n\n")
        answer = input(f"(1) x\n(2) v\n(3) o\n(4) i\n")
        if answer == '3' or answer.lower() == 'v':
            print(f"Yeah. That's correct! 'xovo'\n")
            return True
        else:
            print(f"That's not {answer}. The correct answer is (2) v, with the pattern 'xovo'")
            return False

    if game == 'riddle':
        return challenge_level_one_riddle()
    elif game == 'number':
        return challenge_level_one_number()
    elif game == 'word':
        return challenge_level_one_word()


def main():
    """
    Drive the program.
    """


if __name__ == '__main__':
    main()
