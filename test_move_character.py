from unittest import TestCase
from game import move_character


class TestMoveCharacter(TestCase):
    def test_move_character_top_left_move_down(self):
        player = {'Room': 0, 'Floor': 4, 'Health': 5}
        direction = '3'
        self.assertEqual({'Room': 0, 'Floor': 3, 'Health': 5}, move_character(player, direction))

    def test_move_character_move_left(self):
        second_player = {'Room': 1, 'Floor': 2, 'Health': 5}
        move = '1'
        self.assertEqual({'Room': 0, 'Floor': 2, 'Health': 5}, move_character(second_player, move))

    def test_move_character_move_down(self):
        third_player = {'Room': 1, 'Floor': 4, 'Health': 5}
        move_s = '3'
        self.assertEqual({'Room': 1, 'Floor': 3, 'Health': 5}, move_character(third_player, move_s))
