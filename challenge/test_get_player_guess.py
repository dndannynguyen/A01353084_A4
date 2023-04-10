from unittest import TestCase
from unittest.mock import patch

from final_game import get_player_guess


class TestGetPlayerGuess(TestCase):

    @patch('builtins.input', side_effect=['a'])
    def test_get_player_guess_a(self, _):
        self.assertEqual('a', get_player_guess(10))

    @patch('builtins.input', side_effect=['LoNg'])
    def test_get_player_guess_long(self, _):
        self.assertEqual('long', get_player_guess(23))

    @patch('builtins.input', side_effect=[''])
    def test_get_player_guess_empty(self, _):
        self.assertEqual('', get_player_guess(1))
