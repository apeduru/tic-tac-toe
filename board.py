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
