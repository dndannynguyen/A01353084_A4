from unittest import TestCase
from unittest.mock import patch

from game import check_for_challenge


class TestCheckForFoes(TestCase):

    @patch('random.randint', return_value=3)
    def test_check_for_challenge_random_number_three(self, _):
        self.assertEqual(False, check_for_challenge())

    @patch('random.randint', return_value=2)
    def test_check_for_challenge_random_number_two(self, _):
        self.assertEqual(True, check_for_challenge())

    @patch('random.randint', return_value=1)
    def test_check_for_challenge_random_number_one(self, _):
        self.assertEqual(True, check_for_challenge())
