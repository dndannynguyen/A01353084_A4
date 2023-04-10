import io
from unittest import TestCase
from unittest.mock import patch

from game import describe_current_location


class TestDescribeSimpleLocation(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_first_location(self, mock_stdout):
        first_board = {(2, 2): 'Nakroth'}
        first_character = {'EXP To Level Up': 30, 'Floor': 2, 'Health': 5, 'Level': 1, 'Level One Games':
                           ['riddle', 'word', 'number'], 'Level Two Games': ['riddle', 'word_a', 'word_b', 'number'],
                           'Max Health': 5, 'Name': 'Danny', 'Room': 2}
        describe_current_location(first_board, first_character)
        expected_output = "\nInformation about Danny: \nFloor: 3 |  Room: 3 |  Room Name: Nakroth | Health Point: 5 " \
                          "|  Level: 1 |  EXP To Level Up: 30 \n\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_second_location(self, mock_stdout):
        first_board = {(1, 3): 'Murad'}
        first_character = {'EXP To Level Up': 30, 'Floor': 1, 'Health': 5, 'Level': 1, 'Level One Games':
                           ['riddle', 'word', 'number'], 'Level Two Games': ['riddle', 'word_a', 'word_b', 'number'],
                           'Max Health': 5, 'Name': 'Danny', 'Room': 3}
        describe_current_location(first_board, first_character)
        expected_output = "\nInformation about Danny: \nFloor: 2 |  Room: 4 |  Room Name: Murad | Health Point: 5 " \
                          "|  Level: 1 |  EXP To Level Up: 30 \n\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_third_location(self, mock_stdout):
        first_board = {(0, 4): 'Kriknak'}
        first_character = {'EXP To Level Up': 30, 'Floor': 0, 'Health': 5, 'Level': 1, 'Level One Games':
                           ['riddle', 'word', 'number'], 'Level Two Games': ['riddle', 'word_a', 'word_b', 'number'],
                           'Max Health': 5, 'Name': 'Danny', 'Room': 4}
        describe_current_location(first_board, first_character)
        expected_output = "\nInformation about Danny: \nFloor: 1 |  Room: 5 |  Room Name: Kriknak | Health Point: 5 " \
                          "|  Level: 1 |  EXP To Level Up: 30 \n\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)
