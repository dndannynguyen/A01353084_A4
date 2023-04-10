from unittest import TestCase

from game import is_alive


class TestIsAlive(TestCase):
    def test_is_alive_five_hp(self):
        character = {'Room': 0, 'Floor': 0, 'Health': 5}
        self.assertEqual(True, is_alive(character))

    def test_is_alive_four_hp(self):
        user = {'Room': 0, 'Floor': 3, 'Health': 4}
        self.assertEqual(True, is_alive(user))

    def test_is_alive_two_hp(self):
        gamer = {'Room': 1, 'Floor': 2, 'Health': 2}
        self.assertEqual(True, is_alive(gamer))

    def test_is_alive_one_hp(self):
        character = {'Room': 2, 'Floor': 2, 'Health': 5}
        self.assertEqual(True, is_alive(character))

    def test_is_alive_zero_hp(self):
        loser = {'Room': 2, 'Floor': 1, 'Health': 0}
        self.assertEqual(False, is_alive(loser))
