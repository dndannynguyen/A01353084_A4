from unittest import TestCase
from game import validate_move


class TestValidateMove(TestCase):
    def test_validate_move_top_left_go_up(self):
        first_character = {'Room': 0, 'Floor': 4, 'Current HP': 5}
        first_direction = '2'
        validate_move(first_character, first_direction)
        self.assertEqual(False, validate_move(first_character, first_direction))

    def test_validate_move_top_left_go_left(self):
        my_character = {'Room': 0, 'Floor': 4, 'Current HP': 5}
        my_direction = '1'
        validate_move(my_character, my_direction)
        self.assertEqual(False, validate_move(my_character, my_direction))

    def test_validate_move_top_left_go_right(self):
        the_character = {'Room': 0, 'Floor': 4, 'Current HP': 5}
        the_direction = '4'
        validate_move(the_character, the_direction)
        self.assertEqual(True, validate_move(the_character, the_direction))

    def test_validate_move_top_right_go_left(self):
        first_user = {'Room': 4, 'Floor': 4, 'Current HP': 3}
        first_move = '1'
        validate_move(first_user, first_move)
        self.assertEqual(True, validate_move(first_user, first_move))

    def test_validate_move_bottom_left_go_down(self):
        second_user = {'Room': 0, 'Floor': 0, 'Current HP': 3}
        second_move = '3'
        validate_move(second_user, second_move)
        self.assertEqual(False, validate_move(second_user, second_move))

    def test_validate_move_with_invalid_direction(self):
        the_tester = {'Room': 0, 'Floor': 0, 'Current HP': 3}
        the_move = 'Left'
        validate_move(the_tester, the_move)
        self.assertEqual(False, validate_move(the_tester, the_move))
