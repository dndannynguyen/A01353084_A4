"""
Danny Nguyen
A01353084
"""
import random
from challenge.challenge_level_one import level_one_games
from challenge.challenge_level_two import level_two_games
from challenge.challenge_level_three import level_three_games
from challenge.final_game import final_game


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
    :raise ValueError: if rows or columns or both are not positive integer

    """
    rooms = ['Nakroth', 'Murad', 'Kriknak', 'Elsu', 'Raz', 'Arthur', 'Iggy', 'Xeniel', 'Valhein', 'Aleister']
    return {(row, column): random.choice(rooms) for row in range(rows) for column in range(columns)}


def make_character(name) -> dict:
    """
    Make the character.

    A function that creates a character, with information about character.

    :param name: a string
    :precondition: name must be a string
    :post-condition: correctly creates character information
    :return: a dictionary that contains information about the character
    :raises ValueError: when name is not a string

    >>> player = make_character("Danny")
    >>> player
    {'Name': 'Danny', 'Floor': 4, 'Room': 0, 'Max Health': 5, 'Health': 5, 'Level': 1, 'EXP To Level Up': 30, \
'Level One Games': ['riddle', 'word', 'number'], 'Level Two Games': ['riddle', 'word_a', 'word_b', 'number']}

    >>> user = make_character('Python')
    >>> user
    {'Name': 'Python', 'Floor': 4, 'Room': 0, 'Max Health': 5, 'Health': 5, 'Level': 1, 'EXP To Level Up': 30, \
'Level One Games': ['riddle', 'word', 'number'], 'Level Two Games': ['riddle', 'word_a', 'word_b', 'number']}

    """
    return {'Name': name, 'Floor': 4, 'Room': 0, 'Max Health': 5, 'Health': 5, 'Level': 1, 'EXP To Level Up': 30,
            "Level One Games": ['riddle', 'word', 'number'],
            "Level Two Games": ['riddle', 'word_a', 'word_b', 'number']}


def describe_current_location(board: dict, character: dict) -> None:
    """
    Describe current location and character information.

    A function that tells character information: Floor, Room, Room Name, Health Point, Level, and EXP To Level Up

    :param board: a dictionary
    :param character: a dictionary
    :precondition: board must be a dictionary that has key "Room Name"
    :precondition: character must be a dictionary that has key from the information
    :post-condition: describe the character's current location and information
    :raises ValueError: when board or character or both are not dictionaries
    :raises KeyError: if board or character or both do not have the required key(s)

    """
    name = character["Name"]
    floor = character["Floor"]
    room = character["Room"]
    room_name = board[floor, room]
    hp = character["Health"]
    level = character["Level"]
    next_level = character["EXP To Level Up"]
    print(f"\nInformation about {name}: \n"
          f"Floor: {floor + 1} |  "
          f"Room: {room + 1} |  "
          f"Room Name: {room_name} | "
          f"Health Point: {hp} |  "
          f"Level: {level} |  "
          f"EXP To Level Up: {next_level} \n")


def level_up(character: dict) -> dict:
    """
    Level up the character.

     A function that levels up the character.

    :param character: a dictionary
    :pre-condition: character must have the required keys
    :post-condition: define components to level up and level up the character correctly
    :return: a new dictionary describes character after leveled up
    :raises ValueError: when character is not a dictionary
    :raises KeyError: if character does not have the required key(s)

    >>> player = {'Name': 'Danny', 'Max Health': 5, 'Health': 5, 'Level': 1, 'EXP To Level Up': 10}
    >>> level_up(player)
    {'Name': 'Danny', 'Max Health': 7, 'Health': 5, 'Level': 2, 'EXP To Level Up': 40}

    >>> user = {'Name': 'Python', 'Max Health': 8, 'Health': 2, 'Level': 3, 'EXP To Level Up': 10}
    >>> level_up(user)
    {'Name': 'Python', 'Max Health': 9, 'Health': 5, 'Level': 4, 'EXP To Level Up': 80}

    """
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
    :precondition: character must have 'Floor' as a key
    :precondition: direction must be a string
    :post-condition: define a valid move correctly
    :return: a boolean: True if direction is a valid move; False if direction is not a valid move
    :raises ValueError: if character is not a dictionary and/or direction is not a string
    :raises KeyError: if character does not have a key "Floor"

    >>> valid_move_player = make_character("ValidMover")

    >>> first_direction = '2'
    >>> validate_move(valid_move_player, first_direction)
    False

    >>> second_direction = '4'
    >>> validate_move(valid_move_player, second_direction)
    True

    >>> third_direction = '1'
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
    :precondition: character must be a dictionary that has the required keys
    :precondition: direction must be a string that is a valid move
    :post-condition: define and move the character's coordinates correctly
    :return: the new character dictionary after adjusting the character coordinates
    :raises ValueError: if character is not a dictionary and/or direction is not a string
    :raises KeyError: if character does not have a key "Floor"

    >>> player_move = make_character("Player")
    >>> player_direction = "4"
    >>> after_player_move = move_character(player_move, player_direction)
    >>> after_player_move
    {'Name': 'Player', 'Floor': 4, 'Room': 1, 'Max Health': 5, 'Health': 5, 'Level': 1, 'EXP To Level Up': 30, \
'Level One Games': ['riddle', 'word', 'number'], 'Level Two Games': ['riddle', 'word_a', 'word_b', 'number']}
    >>> user_move = make_character("User")
    >>> user_direction = "3"
    >>> after_user_move = move_character(user_move, user_direction)
    >>> after_user_move
    {'Name': 'User', 'Floor': 3, 'Room': 0, 'Max Health': 5, 'Health': 5, 'Level': 1, 'EXP To Level Up': 30, \
'Level One Games': ['riddle', 'word', 'number'], 'Level Two Games': ['riddle', 'word_a', 'word_b', 'number']}

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

    A function that checks if user reaches floor 1, room 5 and finish the challenge.

    :param character: a dictionary
    :precondition: character must be a dictionary returned by make_character function
    :post-condition: define goal attained correctly
    :return: a boolean: True if goal attained; False if not
    :raises ValueError: if character is not a dictionary
    :raises KeyError if character does not have required keys

    """
    if character["EXP To Level Up"] <= 0:
        level_up(character)
    if character["Floor"] == 0 and character["Room"] == 4 and character["Level"] >= 3:
        print(f"Congratulations! You reached your destination!\n\n"
              f"Now, let's go through your final challenge!\n\n")
        win = final_game(character)
        if win:
            print(f"---------------------------------------------------------------------\n"
                  f"| Congratulations! You finish the final challenge and win the game! |\n"
                  f"---------------------------------------------------------------------")
        else:
            print(f"You lost the game!")
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
    number = random.randint(1, 3)
    if number != 3:
        return True
    else:
        return False


def caution_one_point(character: dict) -> None:
    """
    Give a warning.

    A function that gives player a warning.

    :param character: a dictionary
    :precondition: character must have the key 'Health'
    :post-condition: give user a warning at the right time
    :raises ValueError: if character is not a dictionary
    :raises KeyError: if character does not have the key 'Health'

    """
    if character["Health"] == 1:
        print(f"WARNING: If you get one more wrong guess, you will lose the game! Be careful.\n")


def challenge_in_game(character: dict) -> None:
    """
    A challenge.

    A function that give a challenge that matches character's level.

    :param character: a dictionary
    :precondition: character must have required keys
    :post-condition: define and run the challenge correctly
    :raises ValueError: if character is not a dictionary
    :raises KeyError: if character does not have the required keys

    """
    caution_one_point(character)
    if character["Level"] == 1:
        game_choose_one = random.choice(character["Level One Games"])
        win = level_one_games(game_choose_one)
        if win:
            character["Level One Games"].remove(game_choose_one)
            character["EXP To Level Up"] -= 10
            if character["Health"] < character["Max Health"]:
                character["Health"] += 1
        else:
            character["Health"] -= 1

    elif character["Level"] == 2:
        game_choose_two = random.choice(character["Level Two Games"])
        win = level_two_games(game_choose_two)
        if win:
            character["Level Two Games"].remove(game_choose_two)
            character["EXP To Level Up"] -= 10
            if character["Health"] < character["Max Health"]:
                character["Health"] += 1
        else:
            character["Health"] -= 1
    else:
        win = level_three_games()
        if win:
            character["EXP To Level Up"] -= 10
            if character["Health"] < character["Max Health"]:
                character["Health"] += 1
        else:
            character["Health"] -= 1


def is_alive(character: dict) -> bool:
    """
    Check if the character is still alive.

    A function that checks if character is still alive or not.

    :param character: a dictionary
    :precondition: character must be a dictionary made from make_character function
    :post-condition: define alive correctly
    :return: a boolean: True if character is alive; False if character is not alive
    :raises ValueError: if character is not a dictionary
    :raises KeyError: if character does not have the key 'Health'

    >>> alive_player = make_character("Alive")
    >>> test_alive_player = is_alive(alive_player)
    >>> test_alive_player
    True

    >>> dead_player = make_character("Dead")
    >>> dead_player["Health"] = 0
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
    Runs the challenge.
    """
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    print(f"--------------------------------------------------------------------------------------------------------"
          f"\n\n\n"
          f"Welcome to the challenge!\n"
          f"You need to finish the final challenge at floor 1 room 5 after you reach level 3 to win!\n\n"
          f"(TIPS: Try not to lose mini-challenge. The more health points you have will bring you advantages"
          f"at the final challenge!)\n\n")
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
                challenge_in_game(character)
            achieved_goal = check_if_goal_attained(character)
        else:
            print(f"That's not a valid move. Please try again!\n")
    if not is_alive(character):
        print(f"You lost the game!")


def main():
    """
    Drives the program.
    """

    # challenge()
    game()


if __name__ == "__main__":
    main()
