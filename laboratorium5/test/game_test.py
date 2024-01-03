import unittest
from io import StringIO
from unittest.mock import patch

from laboratorium5.src.game import generate_board, print_board, move_player, game


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.board, self.start_row, self.start_col, self.end_row, self.end_col = generate_board()
        print(self.start_col)
        print(self.start_row)

    def test_board_size(self):
        self.assertEqual(5, len(self.board))
        self.assertEqual(5, len(self.board[0]))

    def test_start_on_boarder(self):
        self.assertTrue(self.start_col == 0 or self.start_row == 0 or
                        self.start_row == 4 or self.start_col == 4)

    def test_stop_on_boarder(self):
        self.assertTrue(self.end_col == 0 or self.end_row == 0 or
                        self.end_row == 4 or self.end_col == 4)

    def test_amount_of_obstacles(self):
        self.assertEqual(sum(row.count('X') for row in self.board), 3)

    def test_print_board(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print_board(self.board)
            printed_board = fake_output.getvalue().strip()
        self.assertIsInstance(printed_board, str)
        self.assertEqual(len(printed_board.split('\n')), 5)

    def test_move_up(self):
        player_row = self.start_row
        player_col = self.start_col

        self.board[player_row][player_col] = '_'
        player_row, player_col = 2, 3
        self.board[player_row - 1][player_col] = '_'
        player_new_row, player_new_col, _, _ = move_player(self.board, 'w',
                                                           player_row, player_col,
                                                           self.start_row, self.start_col)

        self.assertEqual(player_new_row, 1)
        self.assertEqual(player_new_col, 3)

    def test_move_down(self):
        player_row = self.start_row
        player_col = self.start_col

        self.board[player_row][player_col] = '_'
        player_row, player_col = 2, 3
        self.board[player_row + 1][player_col] = '_'
        player_new_row, player_new_col, _, _ = move_player(self.board, 's',
                                                           player_row, player_col,
                                                           self.start_row, self.start_col)

        self.assertEqual(player_new_row, 3)
        self.assertEqual(player_new_col, 3)

    def test_move_left(self):
        player_row = self.start_row
        player_col = self.start_col

        self.board[player_row][player_col] = '_'
        player_row, player_col = 2, 3
        self.board[player_row][player_col - 1] = '_'
        player_new_row, player_new_col, _, _ = move_player(self.board, 'a',
                                                           player_row, player_col,
                                                           self.start_row, self.start_col)

        self.assertEqual(player_new_row, 2)
        self.assertEqual(player_new_col, 2)

    def test_move_right(self):
        player_row = self.start_row
        player_col = self.start_col

        self.board[player_row][player_col] = '_'
        player_row, player_col = 2, 3
        self.board[player_row][player_col + 1] = '_'
        player_new_row, player_new_col, _, _ = move_player(self.board, 'd',
                                                           player_row, player_col,
                                                           self.start_row, self.start_col)

        self.assertEqual(player_new_row, 2)
        self.assertEqual(player_new_col, 4)

    def test_boarder_blockage(self):
        player_row = self.start_row
        player_col = self.start_col

        self.board[player_row][player_col] = '_'
        player_row, player_col = 0, 0
        player_new_row, player_new_col, _, _ = move_player(self.board, 'w',
                                                           player_row, player_col,
                                                           self.start_row, self.start_col)

        self.assertEqual(player_new_row, 0)
        self.assertEqual(player_new_col, 0)

    def test_get_blocked(self):
        player_row = self.start_row
        player_col = self.start_col

        self.board[player_row][player_col] = '_'
        player_row, player_col = 3, 3
        self.board[player_row - 1][player_col] = 'X'
        with patch('sys.stdout', new=StringIO()) as fake_output:
            player_new_row, player_new_col, _, _ = move_player(self.board, 'w',
                                                               player_row, player_col,
                                                               self.start_row, self.start_col)

            printed_content = fake_output.getvalue().strip()
            self.assertEqual(player_new_row, 3)
            self.assertEqual(player_new_row, 3)
            self.assertEqual(printed_content, 'Nie można tam przejść. Jest przeszkoda!')

if __name__ == '__main__':
    unittest.main()
