from pieces import *
from collections import namedtuple
import random

GamePiece = namedtuple('GamePiece', ['val', 'location'])

class GameOverError(Exception):
    pass

class InvalidMoveError(Exception):
    pass

class NewFallerNeededError(Exception):
    pass

possible_shapes = {'I': Iblock,
                   'O': Oblock,
                   'T': Tblock,
                   'S': Sblock,
                   'Z': Zblock,
                   'J': Jblock,
                   'L': Lblock}

class ColumnsGameState:
    def __init__(self) -> None:
        self._rows = 22
        self._columns = 10
        self.board = self._new_game_board(self.get_rows(), self.get_columns())
        self.faller = None

    def get_columns(self) -> int:
        """Returns the number of columns in the board"""
        return self._columns

    def get_rows(self) -> int:
        """Returns the number of rows in the board"""
        return self._rows

    def _new_game_board(self, rows: int, columns: int) -> list[list[int]]:
        """Creates an empty game board with two extra rows at the top to account
        for outside the board matches"""
        board = []
        columns = self.get_columns()
        rows = self.get_rows()

        for col in range(columns):
            board.append([])
            for row in range(rows):
                board[-1].append(GamePiece('_', (col, row)))
        return board

    def check_matches(self) -> list:
        """This will scan the board to check if there are filled rows and return the row numbers"""
        rows = []
        for row in range(self.get_rows()):
            for col in range(self.get_columns()):
                if self.board[col][row].val == '_':
                    break
            else:
                rows.append(row)
        return rows

    def remove_matches(self):
        rows_filled = self.check_matches()
        if len(rows_filled) == 0:
            return 0
        for row in rows_filled:
            self.move_pieces_down(row)
        return len(rows_filled)

    def move_pieces_down(self, row_filled):
        for col in range(self.get_columns()):
            prev = '_'
            for row in range(2, row_filled+1):
                new_prev = self.board[col][row].val
                self.board[col][row] = GamePiece(prev, (col, row))
                prev = new_prev


class Faller:
    def __init__(self, tetro_type: str, game: ColumnsGameState):
        self.type = tetro_type
        self._column = 5
        self.state = "FALLING"
        self.game = game
        self.locations = None
        self.piece = possible_shapes.get(self.type)()
        self.shape = None
        self.cols = None
        self.rows = None
        self.set_starting_point()
        self.put_in_start()

    def can_rotate_left(self):
        self.piece.rotate_left()
        new_shape = self.piece.get_shape()
        new_locations = get_relevant_from_original_shape_matrix(new_shape)
        actual_coords_in_board = []
        for col, row in new_locations:
            actual_coords_in_board.append(self.shape[col][row].location)
        relevant_pieces = self.get_relevant_pieces()
        relevant_locations = [x.location for x in relevant_pieces]
        can_rotate = True
        for col, row in actual_coords_in_board:
            if col < 0 or col > self.game.get_columns() -1:
                can_rotate = False
                break
            if row > self.game.get_rows() -1:
                can_rotate = False
                break
            if self.game.board[col][row].val != '_':
                if (col, row) in relevant_locations:
                    continue
                can_rotate = False
                break
        if not can_rotate:
            self.piece.rotate_right()
        return can_rotate

    def rotate_faller_left(self):
        if self.can_rotate_left():
            temp_shape = self.piece.get_shape()
            previous_locations = {x.location for x in self.get_relevant_pieces()}
            for col in range(self.cols):
                for row in range(self.rows):
                    piece = self.shape[col][row]
                    current_col, current_row = piece.location
                    val = temp_shape[col][row]
                    self.shape[col][row] = GamePiece(val, (current_col, current_row))
            new_locations = {x.location for x in self.get_relevant_pieces()}
            to_remove = previous_locations - new_locations
            to_add = new_locations - previous_locations
            for col, row in to_remove:
                self.game.board[col][row] = GamePiece('_', (col, row))
            for col, row in to_add:
                self.game.board[col][row] = GamePiece(self.type, (col, row))
        if not self.can_drop():
            if self.state == 'FALLING':
                self.state = 'LANDED'
        else:
            self.state = 'FALLING'

    def set_starting_point(self):
        start_col, start_row = None, None
        match self.type:
            case 'O' | 'S':
                start_col = 4
                start_row = 0
            case 'J' | 'L' | 'Z' | 'I' | 'T':
                start_col = 3
                start_row = 0
        self.helper_set_starting(start_col, start_row)

    def helper_set_starting(self, start_col, start_row):
        original = self.piece.get_shape()[:]
        self.rows = len(original[0])
        self.cols = len(original)
        self.shape = []
        for col in range(self.cols):
            _start_row = start_row
            temp_col = []
            for row in range(self.rows):
                val = original[col][row]
                temp_col.append(GamePiece(val,(start_col, _start_row)))
                _start_row += 1
            self.shape.append(temp_col)
            start_col += 1

    def get_relevant_pieces(self):
        ans = []
        for col in range(self.cols):
            for row in range(self.rows):
                if self.shape[col][row].val != '_':
                    ans.append(self.shape[col][row])
        return ans

    def can_drop(self):
        relevant_pieces = self.get_relevant_pieces()
        relevant_locations = [x.location for x in relevant_pieces]
        for piece in relevant_pieces:
            col, row = piece.location
            if row >= self.game.get_rows()-1:
                return False
            if self.game.board[col][row+1].val != '_':
                if (col, row+1) in relevant_locations:
                    continue
                return False
        return True

    def can_move_left(self):
        relevant_pieces = self.get_relevant_pieces()
        relevant_locations = [x.location for x in relevant_pieces]
        for piece in relevant_pieces:
            col, row = piece.location
            if col == 0:
                return False
            if self.game.board[col-1][row].val != '_':
                if (col - 1, row) in relevant_locations:
                    continue
                return False
        return True

    def can_move_right(self):
        relevant_pieces = self.get_relevant_pieces()
        relevant_locations = [x.location for x in relevant_pieces]
        for piece in relevant_pieces:
            col, row = piece.location
            if col == self.game.get_columns() - 1:
                return False
            if self.game.board[col + 1][row].val != '_':
                if (col + 1, row) in relevant_locations:
                    continue
                return False
        return True

    def put_in_start(self):
        if self.can_drop():
            self.drop_faller()
        else:
            raise GameOverError

    def drop_faller(self):
        if self.can_drop():
            previous_locations = {x.location for x in self.get_relevant_pieces()}
            for col in range(self.cols):
                for row in range(self.rows):
                    piece = self.shape[col][row]
                    current_col, current_row = piece.location
                    current_row += 1
                    val = piece.val
                    self.shape[col][row] = GamePiece(val, (current_col, current_row))
            new_locations = {x.location for x in self.get_relevant_pieces()}
            to_remove = previous_locations - new_locations
            to_add = new_locations - previous_locations
            for col, row in to_remove:
                self.game.board[col][row] = GamePiece('_', (col, row))
            for col, row in to_add:
                self.game.board[col][row] = GamePiece(self.type, (col, row))
        elif self.state == 'FALLING':
            self.state = 'LANDED'
        elif self.state == 'LANDED':
            self.state = 'FROZEN'
        else:
            raise NewFallerNeededError

    def move_faller_left(self):
        if self.can_move_left():
            previous_locations = {x.location for x in self.get_relevant_pieces()}
            for col in range(self.cols):
                for row in range(self.rows):
                    piece = self.shape[col][row]
                    current_col, current_row = piece.location
                    current_col -= 1
                    val = piece.val
                    self.shape[col][row] = GamePiece(val, (current_col, current_row))
            new_locations = {x.location for x in self.get_relevant_pieces()}
            to_remove = previous_locations - new_locations
            to_add = new_locations - previous_locations
            for col, row in to_remove:
                self.game.board[col][row] = GamePiece('_', (col, row))
            for col, row in to_add:
                self.game.board[col][row] = GamePiece(self.type, (col, row))
        if not self.can_drop():
            if self.state == 'FALLING':
                self.state = 'LANDED'
        else:
            self.state = 'FALLING'

    def move_faller_right(self):
        if self.can_move_right():
            previous_locations = {x.location for x in self.get_relevant_pieces()}
            for col in range(self.cols):
                for row in range(self.rows):
                    piece = self.shape[col][row]
                    current_col, current_row = piece.location
                    current_col += 1
                    val = piece.val
                    self.shape[col][row] = GamePiece(val, (current_col, current_row))
            new_locations = {x.location for x in self.get_relevant_pieces()}
            to_remove = previous_locations - new_locations
            to_add = new_locations - previous_locations
            for col, row in to_remove:
                self.game.board[col][row] = GamePiece('_', (col, row))
            for col, row in to_add:
                self.game.board[col][row] = GamePiece(self.type, (col, row))
        if not self.can_drop():
            if self.state == 'FALLING':
                self.state = 'LANDED'
        else:
            self.state = 'FALLING'

    def can_rotate_right(self):
        self.piece.rotate_right()
        new_shape = self.piece.get_shape()
        new_locations = get_relevant_from_original_shape_matrix(new_shape)
        actual_coords_in_board = []
        for col, row in new_locations:
            actual_coords_in_board.append(self.shape[col][row].location)
        relevant_pieces = self.get_relevant_pieces()
        relevant_locations = [x.location for x in relevant_pieces]
        can_rotate = True
        for col, row in actual_coords_in_board:
            if col < 0 or col > self.game.get_columns() - 1:
                can_rotate = False
                break
            if row > self.game.get_rows() - 1:
                can_rotate = False
                break
            if self.game.board[col][row].val != '_':
                if (col, row) in relevant_locations:
                    continue
                can_rotate = False
                break
        if not can_rotate:
            self.piece.rotate_left()
        return can_rotate

    def rotate_faller_right(self):
        if self.can_rotate_right():
            temp_shape = self.piece.get_shape()
            previous_locations = {x.location for x in self.get_relevant_pieces()}
            for col in range(self.cols):
                for row in range(self.rows):
                    piece = self.shape[col][row]
                    current_col, current_row = piece.location
                    val = temp_shape[col][row]
                    self.shape[col][row] = GamePiece(val, (current_col, current_row))
            new_locations = {x.location for x in self.get_relevant_pieces()}
            to_remove = previous_locations - new_locations
            to_add = new_locations - previous_locations
            for col, row in to_remove:
                self.game.board[col][row] = GamePiece('_', (col, row))
            for col, row in to_add:
                self.game.board[col][row] = GamePiece(self.type, (col, row))
        if not self.can_drop():
            if self.state == 'FALLING':
                self.state = 'LANDED'
        else:
            self.state = 'FALLING'

def get_relevant_from_original_shape_matrix(matrix):
    ans = []
    for col in range(len(matrix)):
        for row in range(len(matrix[col])):
            if matrix[col][row] != '_':
                ans.append((col, row))
    return ans

class Randomizer:
    def __init__(self, game):
        self.possible = ['I', 'O', 'T', 'S', 'Z', 'J', 'L']
        self.game = game
        self.current_bag = self.possible[:]

    def create_random_faller(self):
        if len(self.current_bag) == 0:
            self.current_bag = self.possible[:]
        choice = random.choices(self.current_bag)[0]
        self.current_bag.pop(self.current_bag.index(choice))
        return Faller(choice, self.game)