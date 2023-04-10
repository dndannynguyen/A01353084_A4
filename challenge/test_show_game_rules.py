import io
from unittest import TestCase
from unittest.mock import patch

from final_game import show_game_rules


class TestShowGameRules(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_game_rules_twelve(self, mock_output):
        show_game_rules(12)
        the_game_printed_this = mock_output.getvalue()
        expected_output = "\n\nWelcome to THE FINAL CHALLENGE!\n\nWe have the hidden word showed as '_ _ _'." \
                          "\nYou have to enter the letter that you guess would appear in the word." \
                          "\nYou can only make 7 wrong guesses. " \
                          "\nBut we added your health remaining, you now have 12 wrong guesses." \
                          "\n\nWARNING: This is a final challenge, " \
                          "so if you lose this, you will lose the game!\n"
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_game_rules_nine(self, mock_output):
        show_game_rules(9)
        the_game_printed_this = mock_output.getvalue()
        expected_output = "\n\nWelcome to THE FINAL CHALLENGE!\n\nWe have the hidden word showed as '_ _ _'." \
                          "\nYou have to enter the letter that you guess would appear in the word." \
                          "\nYou can only make 7 wrong guesses. " \
                          "\nBut we added your health remaining, you now have 9 wrong guesses." \
                          "\n\nWARNING: This is a final challenge, " \
                          "so if you lose this, you will lose the game!\n"
        self.assertEqual(expected_output, the_game_printed_this)
