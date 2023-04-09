"""
Danny Nguyen
A01353084
"""


def level_two_games(game):

    def challenge_level_two_number():
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
        print(f"Welcome to the Intermediate Word Game! \n\n"
              f"Retype the word below to cover the '_': \n\n"
              f"J_v_s_rip_")
        answer = input(f"Answer: ")
        if answer.lower() == 'javascript' or answer.lower() == 'aact':
            print(f"Yeah. That's correct! 'Javascript'\n")
            return True
        else:
            print(f"That's not {answer}. The correct answer is 'Javascript'.")
            return False

    def challenge_level_two_word_b():
        print(f"Welcome to the Intermediate Word Game! \n\n"
              f"Retype the word below to cover the '_': \n\n"
              f"c_a_gp_")
        answer = input(f"Answer: ")
        if answer.lower().strip() == 'chatgpt' or answer.lower() == 'htt':
            print(f"Yeah. That's correct! 'chatgpt'\n")
            return True
        else:
            print(f"That's not {answer}. The correct answer is 'chatgpt'.")
            return False

    def challenge_level_two_riddle():
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