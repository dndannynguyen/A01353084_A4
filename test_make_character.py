from unittest import TestCase
from game import make_character


class TestMakeCharacter(TestCase):
    def test_make_character(self):
        player = make_character("Danny")
        expected_output = {'EXP To Level Up': 30, 'Floor': 4, 'Health': 5, 'Level': 1, 'Level One Games':
                           ['riddle', 'word', 'number'], 'Level Two Games': ['riddle', 'word_a', 'word_b', 'number'],
                           'Max Health': 5, 'Name': 'Danny', 'Room': 0}
        self.assertEqual(expected_output, player)
