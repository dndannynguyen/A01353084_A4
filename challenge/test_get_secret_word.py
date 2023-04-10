from unittest import TestCase
from unittest.mock import patch

from challenge_level_three import get_secret_word
from final_game import get_secret_word


class TestGetSecretWord(TestCase):

    @patch('random.choice', side_effect=['international'])
    def test_get_secret_word_international(self, _):
        self.assertEqual('international', get_secret_word())

    @patch('random.choice', side_effect=['concatenation'])
    def test_get_secret_word_concatenation(self, _):
        self.assertEqual('concatenation', get_secret_word())

    @patch('random.choice', side_effect=['immutable'])
    def test_get_secret_word_immutable(self, _):
        self.assertEqual('immutable', get_secret_word())
