#!/usr/bin/python3


class Board(object):

    def __init__(self):
        self.pieces = {
            "TL": " ",
            "TM": " ",
            "TR": " ",
            "ML": " ",
            "MM": " ",
            "MR": " ",
            "BL": " ",
            "BM": " ",
            "BR": " ",
        }
        self.board = [["TL", "TM", "TR"],
                      ["ML", "MM", "MR"],
                      ["BL", "BM", "BR"]]

        self.spaces = len(self.pieces)
        self.empty_spaces = self.spaces
        self.occupied_spaces = 0

    @property
    def filled(self):
        return self.spaces == self.occupied_spaces

    @property
    def empty(self):
        return self.occupied_spaces == 0

    def build_board(self):
        board = []
        blank = " "
        v = "|"
        h = "-"
        for space in self.board:
            board.append(blank * 5 + v + blank * 5 + v + blank * 5)
            board.append(blank * 2 + self.pieces[space[0]] + blank * 2 + v +
                         blank * 2 + self.pieces[space[1]] + blank * 2 + v +
                         blank * 2 + self.pieces[space[2]] + blank * 2)
            board.append(blank * 5 + v + blank * 5 + v + blank * 5)
            if space == self.board[2]:
                break
            board.append(h * 20)

        board = "\n".join(board)
        print(board)

    def place_piece(self, space, piece):
        self.pieces[space] = piece
        self.empty_spaces -= 1
        self.occupied_spaces += 1

    def calculate_column(self, current_piece):
        board = self.board
        # Transpose the board matrix to access columns easier
        board = list(map(list, zip(*board)))
        pieces = self.pieces
        for column in board:
            if all(pieces[piece] == current_piece for piece in column):
                return True
        return False

    def calculate_row(self, current_piece):
        board = self.board
        pieces = self.pieces
        for row in board:
            if all(pieces[piece] == current_piece for piece in row):
                return True
        return False

    def calculate_diag(self, current_piece):
        board = self.board
        pieces = self.pieces
        main_diag = [board[i][i] for i in range(len(board))]
        anti_diag = [board[i][2 - i] for i in range(len(board))]

        if all(pieces[piece] == current_piece for piece in main_diag):
            return True
        if all(pieces[piece] == current_piece for piece in anti_diag):
            return True
        return False

    def available_moves(self):
        moves = [m for (m, p) in self.pieces.items() if p is " "]
        assert len(moves) == self.empty_spaces
        return sorted(moves)

    def occupied_spaces(self):
        spaces = [m for (m, p) in self.pieces.items() if p is not " "]
        assert len(spaces) == self.occupied_spaces
        return sorted(spaces)

    def display_available_moves(self):
        moves = self.available_moves()
        moves = ", ".join(str(move) for move in moves)
        print("Available moves: {}".format(moves))


