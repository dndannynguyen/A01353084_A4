from unittest import TestCase
from game import level_up


class TestLevelUp(TestCase):
    def test_level_up(self):
        player = {'EXP To Level Up': 10, 'Floor': 4, 'Health': 5, 'Level': 1, 'Level One Games':
                  ['riddle', 'word', 'number'], 'Level Two Games': ['riddle', 'word_a', 'word_b', 'number'],
                  'Max Health': 5, 'Name': 'Danny', 'Room': 0}

        expected_output = {'EXP To Level Up': 40, 'Floor': 4, 'Health': 5, 'Level': 2, 'Level One Games':
                           ['riddle', 'word', 'number'], 'Level Two Games': ['riddle', 'word_a', 'word_b', 'number'],
                           'Max Health': 7, 'Name': 'Danny', 'Room': 0}
        self.assertEqual(expected_output, level_up(player))

    def test_grow_up(self):
        user = {'EXP To Level Up': 10, 'Floor': 4, 'Health': 5, 'Level': 3, 'Level One Games':
                ['riddle', 'word', 'number'], 'Level Two Games': ['riddle', 'word_a', 'word_b', 'number'],
                'Max Health': 5, 'Name': 'Danny', 'Room': 0}

        expected_output = {'EXP To Level Up': 80, 'Floor': 4, 'Health': 5, 'Level': 4, 'Level One Games':
                           ['riddle', 'word', 'number'], 'Level Two Games': ['riddle', 'word_a', 'word_b', 'number'],
                           'Max Health': 9, 'Name': 'Danny', 'Room': 0}
        self.assertEqual(expected_output, level_up(user))

    def test_level_up_six(self):
        player = {'EXP To Level Up': 10, 'Floor': 4, 'Health': 5, 'Level': 5, 'Level One Games':
                  ['riddle', 'word', 'number'], 'Level Two Games': ['riddle', 'word_a', 'word_b', 'number'],
                  'Max Health': 5, 'Name': 'Danny', 'Room': 0}

        expected_output = {'EXP To Level Up': 120, 'Floor': 4, 'Health': 5, 'Level': 6, 'Level One Games':
                           ['riddle', 'word', 'number'], 'Level Two Games': ['riddle', 'word_a', 'word_b', 'number'],
                           'Max Health': 11, 'Name': 'Danny', 'Room': 0}
        self.assertEqual(expected_output, level_up(player))
