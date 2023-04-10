import io
from unittest import TestCase
from unittest.mock import patch
from game import check_if_goal_attained


class TestCheckIfGoalAttained(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_goal_not_attained(self, mock_stdout):
        player = {'Room': 0, 'Floor': 0, 'Health': 5, "EXP To Level Up": 20}
        the_game_printed_this = mock_stdout.getvalue()
        self.assertEqual(False, check_if_goal_attained(player), the_game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_goal_attained(self, mock_stdout):
        user = {'Room': 2, 'Floor': 0, 'Health': 5, "EXP To Level Up": 0, "Level": 3}
        the_game_printed_this = mock_stdout.getvalue()
        self.assertEqual(False, check_if_goal_attained(user), the_game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_in_the_middle(self, mock_stdout):
        tester = {'Room': 1, 'Floor': 1, 'Health': 5, "EXP To Level Up": 30}
        the_game_printed_this = mock_stdout.getvalue()
        self.assertEqual(False, check_if_goal_attained(tester), the_game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_if_goal_attained_when_top_right(self, mock_stdout):
        gamer = {'Room': 2, 'Floor': 0, 'Health': 5, "EXP To Level Up": 0, "Level": 2}
        the_game_printed_this = mock_stdout.getvalue()
        self.assertEqual(False, check_if_goal_attained(gamer), the_game_printed_this)
