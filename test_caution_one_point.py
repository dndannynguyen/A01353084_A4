import io
from unittest import TestCase
from unittest.mock import patch

from game import caution_one_point


class TestCautionOnePoint(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_caution_one_point_warn(self, mock_stdout):
        player = {'Health': 1}
        caution_one_point(player)
        the_game_printed_this = mock_stdout.getvalue()

        self.assertEqual(None, caution_one_point(player), the_game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_caution_one_point_no_warning(self, mock_stdout):
        user = {'Health': 1}
        caution_one_point(user)
        the_game_printed_this = mock_stdout.getvalue()

        self.assertEqual(None, caution_one_point(user), the_game_printed_this)
