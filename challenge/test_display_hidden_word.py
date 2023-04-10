import io
from unittest import TestCase
from unittest.mock import patch

from final_game import display_hidden_word


class TestDisplayHiddenWord(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_hidden_word_a(self, mock_output):
        display_hidden_word('algorithm', 'a')
        the_game_printed_this = mock_output.getvalue()
        expected_output = '\nThe hidden word: a _ _ _ _ _ _ _ _ \n'
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_hidden_word_no(self, mock_output):
        display_hidden_word('algorithm', 'z')
        the_game_printed_this = mock_output.getvalue()
        expected_output = '\nThe hidden word: _ _ _ _ _ _ _ _ _ \n'
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_hidden_word_multiple(self, mock_output):
        display_hidden_word('canada', 'a')
        the_game_printed_this = mock_output.getvalue()
        expected_output = '\nThe hidden word: _ a _ a _ a \n'
        self.assertEqual(expected_output, the_game_printed_this)
