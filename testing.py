from game_logic import *
import unittest


def insert_pieces(pieces, game):
    for col, row in pieces:
        game.board[col][row] = GamePiece('n', (col, row))


def print_board(game):
    for row in range(2, game.get_rows()):
        for col in range(game.get_columns()):
            print(game.board[col][row].val, end = ' ')
        print()


class Tests(unittest.TestCase):

    # def test_matching(self):
    #     game = ColumnsGameState()
    #     for col in range(game.get_columns()):
    #         game.board[col][8] = GamePiece('n', (col, 8))
    #     match = game.check_matches()
    #     self.assertEqual([8], match)
    #
    # def test_faller_creation(self):
    #     game = ColumnsGameState()
    #     faller = Faller('I', game)
    #     self.assertEqual('I', faller.type)
    #     self.assertEqual(Iblock, type(faller.piece))
    #
    # def test_faller_I_start(self):
    #     game = ColumnsGameState()
    #     faller = Faller('T', game)
    #     insert_pieces([(3,3)], game)
    #     self.assertFalse(faller.can_drop())
    #
    # def test_faller_can_drop(self):
    #     game = ColumnsGameState()
    #     faller = Faller('T', game)
    #     self.assertTrue(faller.can_drop())
    #
    # def test_faller_drop(self):
    #     game = ColumnsGameState()
    #     faller = Faller('O', game)
    #     faller.drop_faller()
    #     for i in range(19):
    #         faller.drop_faller()
    #     self.assertEqual('LANDED', faller.state)
    #     faller.drop_faller()
    #     self.assertEqual('FROZEN', faller.state)
    #     with self.assertRaises(NewFallerNeededError):
    #         faller.drop_faller()
    #
    # def test_faller_move_left(self):
    #     game = ColumnsGameState()
    #     faller = Faller('T', game)
    #     faller.drop_faller()
    #     faller.move_faller_left()

    def test_faller_rotate_left(self):
        game = ColumnsGameState()
        faller = Faller('T', game)

    def test_randomizer(self):
        game = ColumnsGameState()
        randomizer = Randomizer(game)
        # for i in range(14):
        #     randomizer.create_random_faller()


if __name__ == '__main__':
    unittest.main()