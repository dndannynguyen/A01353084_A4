from unittest import TestCase
from unittest.mock import patch

from game import make_board


class TestMakeBoard(TestCase):
    @patch('random.choice', side_effect=['Nakroth', 'Murad', 'Kriknak', 'Elsu'])
    def test_make_board_two_two(self, _):
        first_row = 2
        first_column = 2
        board = make_board(first_row, first_column)
        expected_board = {(0, 0): 'Nakroth', (0, 1): 'Murad', (1, 0): 'Kriknak', (1, 1): 'Elsu'}
        self.assertEqual(board, expected_board)

    @patch('random.choice', side_effect=['Murad', 'Kriknak', 'Elsu', 'Xeniel', 'Nakroth', 'Valhein', 'Arthur', 'Raz',
                                         'Iggy', 'Aleister', 'Raz', 'Elsu', 'Xeniel', 'Kriknak', 'Valhein', 'Nakroth',
                                         'Iggy', 'Murad', 'Arthur', 'Raz', 'Kriknak', 'Aleister', 'Xeniel',
                                         'Elsu', 'Valhein'])
    def test_make_board_five_five(self, _):
        second_row = 5
        second_column = 5
        board = make_board(second_row, second_column)
        expected_board = {(0, 0): 'Murad', (0, 1): 'Kriknak', (0, 2): 'Elsu', (0, 3): 'Xeniel', (0, 4): 'Nakroth',
                          (1, 0): 'Valhein', (1, 1): 'Arthur', (1, 2): 'Raz', (1, 3): 'Iggy', (1, 4): 'Aleister',
                          (2, 0): 'Raz', (2, 1): 'Elsu', (2, 2): 'Xeniel', (2, 3): 'Kriknak', (2, 4): 'Valhein',
                          (3, 0): 'Nakroth', (3, 1): 'Iggy', (3, 2): 'Murad', (3, 3): 'Arthur', (3, 4): 'Raz',
                          (4, 0): 'Kriknak', (4, 1): 'Aleister', (4, 2): 'Xeniel', (4, 3): 'Elsu', (4, 4): 'Valhein'}
        self.assertEqual(board, expected_board)

    @patch('random.choice', side_effect=['Elsu', 'Kriknak', 'Iggy', 'Valhein', 'Nakroth', 'Xeniel', 'Arthur',
                                         'Raz', 'Murad', 'Aleister', 'Elsu', 'Kriknak'])
    def test_make_board_four_three(self, _):
        third_row = 4
        third_column = 3
        board = make_board(third_row, third_column)
        expected_board = {(0, 0): 'Elsu', (0, 1): 'Kriknak', (0, 2): 'Iggy', (1, 0): 'Valhein', (1, 1): 'Nakroth',
                          (1, 2): 'Xeniel', (2, 0): 'Arthur', (2, 1): 'Raz', (2, 2): 'Murad',
                          (3, 0): 'Aleister', (3, 1): 'Elsu', (3, 2): 'Kriknak'}
        self.assertEqual(board, expected_board)
