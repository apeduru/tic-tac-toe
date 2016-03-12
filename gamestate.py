#!/usr/bin/python3

import os
# import time
import random
from board import Board
from player import Player, AI


class GameState(object):

    def __init__(self, game_type, p1n, p2n="AI"):
        self.p1 = Player(p1n, "X")
        if (game_type == 'ai'):
            self.p2 = AI(self, p2n, "O")
        elif (game_type == 'pvp'):
            self.p2 = Player(p2n, "O")
        self.board = Board()
        self.state = False
        self.winner = None
        self.current = None

    @property
    def board_filled(self):
        return self.board.filled

    def build_board(self):
        self.board.build_board()

    def decide_first_move(self, p1, p2):
        self.current = random.choice([p1, p2])

    def get_next_move(self):
        if self.current is None:
            self.decide_first_move(self.p1, self.p2)

        while (True):
            self.board.build_board()
            self.display_available_moves()
            moves = self.available_moves()
            move = self.current.turn()
            if (len(move) == 2 and move in moves):
                break
            os.system('clear')

        self.make_move(move)
        if (self.calculate_row() or self.calculate_column() or
                self.calculate_diag()):
            self.declare_winner(self.current)
            return

        if self.current == self.p1:
            self.current = self.p2
        else:
            self.current = self.p1

    def make_move(self, move):  # kek
        self.board.place_piece(move, self.current.piece)

    def available_moves(self):
        moves = sorted([m for (m, p) in self.board.pieces.items() if p is " "])
        assert len(moves) == self.board.empty_spaces
        return moves

    def occupied_spaces(self):
        spaces = sorted(
            [m for (m, p) in self.board.pieces.items() if p is not " "])
        assert len(spaces) == self.board.occupied_spaces
        return spaces

    def display_available_moves(self):
        moves = self.available_moves()
        moves = ", ".join(str(move) for move in moves)
        print("Available moves: {}".format(moves))

    def calculate_column(self):
        board = self.board.board
        # Transpose the board matrix to access columns easier
        board = list(map(list, zip(*board)))
        pieces = self.board.pieces
        for column in board:
            if all(pieces[piece] == self.current.piece for piece in column):
                return True
        return False

    def calculate_row(self):
        board = self.board.board
        pieces = self.board.pieces
        for row in board:
            if all(pieces[piece] == self.current.piece for piece in row):
                return True
        return False

    def calculate_diag(self):
        board = self.board.board
        pieces = self.board.pieces
        major_diag = [board[i][i] for i in range(len(board))]
        minor_diag = [board[i][2 - i] for i in range(len(board))]

        if all(pieces[piece] == self.current.piece for piece in major_diag):
            return True
        if all(pieces[piece] == self.current.piece for piece in minor_diag):
            return True
        return False

    def declare_winner(self, winner):
        self.winner = winner

    @property
    def game_over(self):
        return self.board_filled or self.winner
