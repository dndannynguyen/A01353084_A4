import io
from unittest import TestCase
from unittest.mock import patch

from game import get_user_choice


class TestGetUserChoice(TestCase):

    @patch('builtins.input', side_effect=['w'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_w(self, _, mock_stdout):
        user_input_w = get_user_choice()
        the_game_printed_this = mock_stdout.getvalue()
        self.assertEqual('w', user_input_w, the_game_printed_this)

    @patch('builtins.input', side_effect=['LeFT'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_north(self, _, mock_stdout):
        user_input_north = get_user_choice()
        the_game_printed_this = mock_stdout.getvalue()
        self.assertEqual('left', user_input_north, the_game_printed_this)

    @patch('builtins.input', side_effect=['To The Left', 'RigHt'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_invalid(self, _, mock_stdout):
        user_input_invalid = get_user_choice()
        the_game_printed_this = mock_stdout.getvalue()
        self.assertEqual('right', user_input_invalid, the_game_printed_this)

    @patch('builtins.input', side_effect=['To The Right', 'knot', 'sound', 'eat', 'down'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_multiple_invalid(self, _, mock_stdout):
        user_input_invalid = get_user_choice()
        the_game_printed_this = mock_stdout.getvalue()
        self.assertEqual('down', user_input_invalid, the_game_printed_this)
