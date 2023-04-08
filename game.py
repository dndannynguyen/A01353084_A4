"""
Danny Nguyen
A01353084
"""
import random


def make_board(rows: int, columns: int) -> dict:
    """
    Make the board.

    A function that makes the board with name for each room in the board.

    :param rows: a positive integer
    :param columns: a positive integer
    :precondition: rows must be a positive integer greater than or equal to two
    :precondition: columns must be a positive integer greater than or equal to two
    :post-condition: define, make the board correctly, and randomly assign the name for each existed room
    :return: a dictionary that contains coordinates of the rooms in a tuple equivalent to the name of the room

    """
    rooms = ['Nakroth', 'Murad', 'Kriknak', 'Elsu', 'Raz', 'Arthur', 'Iggy', 'Xeniel', 'Valhein', 'Aleister']
    return {(row, column): random.choice(rooms) for row in range(rows) for column in range(columns)}


def make_character(name) -> dict:
    """
    Make the character.

    A function that creates a character, with the starting coordinates and HP.

    :return: a dictionary that contains "Floor" and "Room" are equal to 0, "Current HP" is equal to 5

    >>> player = make_character()
    >>> player
    {'Floor': 0, 'Room': 0, 'Current HP': 5}

    >>> user = make_character()
    >>> user
    {'Floor': 0, 'Room': 0, 'Current HP': 5}

    """
    return {'Name': name, 'Floor': 4, 'Room': 0, 'Max Health': 5, 'Health': 5, 'Level': 1, 'EXP To Level Up': 30}


def describe_current_location(board: dict, character: dict) -> None:
    """
    Describe current location.

    A function that tells which row and column the user at, with the name of the room and HP user has left.

    :param board: a dictionary
    :param character: a dictionary
    :precondition: board must be a dictionary that is created by make_board function
    :precondition: character must be a dictionary that is created by make_character function
    :post-condition: define and describe the row, column, room, and HP level the character at

    """
    name = character["Name"]
    floor = character["Floor"]
    room = character["Room"]
    hp = character["Health"]
    level = character["Level"]
    next_level = character["EXP To Level Up"]
    print(f"{name} is at floor {floor+1}, room {room+1}, The {board[(floor, room)]},"
          f" with {hp} health point(s) remaining, and {next_level} experience points to level up."
          f"You are level {level}")


def level_up(character: dict) -> dict:
    character["Level"] += 1
    character["Max Health"] = 5 + character["Level"]
    character["EXP To Level Up"] = 20 * character["Level"]
    if character["Health"] <= 5:
        character["Health"] = 5
    return character


def get_user_choice() -> str:
    """
    Get user choice.

    A function that gets the user's choice for which direction they are moving next.
    :post-condition: define the valid keys and each move correctly
    :return: the direction user wants to move

    """
    while True:
        user_input = (input("Direction to move:\n1. [<] Left\n2. [^] Up\n3. [v] Down\n4. [>] Right\n")).lower()
        if user_input in ("up", "w", "down", "s", "right", "d", "left", "a", "1", "2", "3", "4"):
            break
        else:
            print(f"'{user_input}' is not defined as a valid key to move.\n")
    return user_input


def validate_move(character: dict, direction: str) -> bool:
    """
    Check if direction user want to go is valid.

    A function that checks if direction user wants to go is a valid move.

    :param character: a dictionary
    :param direction: a string
    :precondition: character must be created by make_character function
    :precondition: direction must be a string returned by get_user_choice function
    :post-condition: define a valid move correctly
    :return: a boolean: True if direction is a valid move; False if direction is not a valid move

    >>> valid_move_player = make_character()

    >>> first_direction = 'n'
    >>> validate_move(valid_move_player, first_direction)
    False

    >>> second_direction = 's'
    >>> validate_move(valid_move_player, second_direction)
    True

    >>> third_direction = 'w'
    >>> validate_move(valid_move_player, third_direction)
    False

    """
    if character["Floor"] == 4 and direction in ("up", "w", "2"):
        return False
    elif character["Floor"] == 0 and direction in ("down", "s", "3"):
        return False
    elif character["Room"] == 0 and direction in ("left", "a", "1"):
        return False
    elif character["Room"] == 4 and direction in ("right", "d", "4"):
        return False
    else:
        if direction in ("up", "w", "down", "s", "right", "d", "left", "a", "1", "2", "3", "4"):
            return True
        else:
            return False


def move_character(character: dict, direction: str) -> dict:
    """
    Move the character.

    A function that moves the character to the direction the user wants.

    :param character: a dictionary
    :param direction: a string
    :precondition: character must be a dictionary that is generated by make_character function
    :precondition: direction must be a string returned by get_user_choice function
    :post-condition: define and move the character's coordinates correctly
    :return: the new character dictionary after adjusting the character coordinates

    >>> player_move = make_character()
    >>> player_direction = "s"
    >>> after_player_move = move_character(player_move, player_direction)
    >>> after_player_move
    {'Floor': 0, 'Room': 1, 'Current HP': 5}

    >>> user_move = make_character()
    >>> user_direction = "e"
    >>> after_user_move = move_character(user_move, user_direction)
    >>> after_user_move
    {'Floor': 1, 'Room': 0, 'Current HP': 5}

    >>> tester_move = make_character()
    >>> tester_direction = "s"
    >>> later_tester_move = move_character(tester_move, tester_direction)
    >>> later_tester_move
    {'Floor': 0, 'Room': 1, 'Current HP': 5}

    """
    if direction in ("up", "w", "2"):
        character["Floor"] += 1
    elif direction in ("down", "s", "3"):
        character["Floor"] -= 1
    elif direction in ("right", "d", "4"):
        character["Room"] += 1
    elif direction in ("left", "a", "1"):
        character["Room"] -= 1
    return character


def check_if_goal_attained(character: dict) -> bool:
    """
    Check if goal attained.

    A function that checks if user reaches row 2 column 2.

    :param character: a dictionary
    :precondition: character must be a dictionary returned by make_character function
    :post-condition: define goal attained correctly
    :return: a boolean: True if goal attained; False if not

    >>> win_player = make_character()
    >>> win_player["Floor"] = 4
    >>> win_player["Room"] = 4
    >>> check_win = check_if_goal_attained(win_player)
    Congratulations! You reached your destination!
    >>> check_win
    True

    >>> not_win_player = make_character()
    >>> not_win_player["Floor"] = 1
    >>> not_win_player["Room"] = 2
    >>> check_not_win = check_if_goal_attained(not_win_player)
    >>> check_not_win
    False

    """
    if character["EXP To Level Up"] <= 0:
        level_up(character)
    if character["Floor"] == 0 and character["Room"] == 4 and character["Level"] >= 3:
        print(f"Congratulations! You reached your destination!")
        return True
    else:
        return False


def check_for_challenge() -> bool:
    """
    Check for challenge.

    A function that checks if challenge is in the room or not.

    :post-condition: define and randomly assign challenge
    :return: a boolean: True if there are challenge; False if not

    """
    number = random.randint(1, 2)
    if number == 1:
        return True
    else:
        return False


def caution_one_point(character):
    if character["Health"] == 1:
        print(f"WARNING: If you get one more wrong guess, you will lose the game! Be careful.\n")


def guessing_game(character: dict, upper: int) -> None:
    """
    A guessing game.

    A function that creates a game that requires user to guess a random number generated.

    :param character: a dictionary
    :param upper: an integer
    :precondition: character must be a dictionary that is returned by make_character function
    :precondition: upper must be a non-zero positive integer
    :post-condition: define and run the game correctly

    """
    secret_number = str(random.randint(1, upper))
    print(f"Opponents ahead! Guess the correct number to beat them.\n")
    caution_one_point(character)
    guess = input(f"Enter a number from 1 to {upper}: ")
    if guess == secret_number:
        character["EXP To Level Up"] -= 10
        if character["Health"] < character["Max Health"]:
            character["Health"] += 1
        print(f"You're right! It's {guess}.\n")
    else:
        print(f"It's {secret_number}. You guessed it wrong! Losing 1 HP.\n")
        character["Health"] -= 1
        caution_one_point(character)


def is_alive(character: dict) -> bool:
    """
    Check if the character is still alive.

    A function that checks if character is still alive or not.

    :param character: a dictionary
    :precondition: character must be a dictionary made from make_character function
    :post-condition: define alive correctly
    :return: a boolean: True if character is alive; False if character is not alive

    >>> alive_player = make_character()
    >>> test_alive_player = is_alive(alive_player)
    >>> test_alive_player
    True

    >>> dead_player = make_character()
    >>> dead_player["Current HP"] = 0
    >>> test_dead_player = is_alive(dead_player)
    >>> test_dead_player
    False

    """
    if character["Health"] <= 0:
        return False
    else:
        return True


def game() -> None:
    """
    Runs the game.
    """
    rows = 5
    columns = 5
    upper = 1
    board = make_board(rows, columns)
    print(f"--------------------------------------------------------------------------------------------------------"
          f"\n\n\n"
          f"Welcome to the game!\n"
          f"You need to beat the boss at floor 1 room 5 after you reach level 3 to win!\n")
    name = input('Enter your user name: ')
    character = make_character(name)
    achieved_goal = False
    while not achieved_goal and is_alive(character):
        describe_current_location(board, character)
        direction = get_user_choice()
        valid_move = validate_move(character, direction)
        if valid_move:
            move_character(character, direction)
            there_is_a_challenger = check_for_challenge()
            if there_is_a_challenger:
                guessing_game(character, upper)
            achieved_goal = check_if_goal_attained(character)
        else:
            print(f"That's not a valid move. Please try again!\n")
    if not is_alive(character):
        print(f"You lost the game!")


def main():
    """
    Drives the program.
    """

    game()


if __name__ == "__main__":
    main()
