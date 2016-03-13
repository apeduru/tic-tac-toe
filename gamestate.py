#!/usr/bin/python3

import os
# import time
import random
from player import Player, AI


class GameState(object):

    def __init__(self, game_type, board, p1n, p2n="AI"):
        self.board = board
        self.winner = None
        self.current = None

        self.p1 = Player(p1n, "X")
        if (game_type == 'ai'):
            self.p2 = AI(board, p2n, "O")
        elif (game_type == 'pvp'):
            self.p2 = Player(p2n, "O")

    @property
    def board_filled(self):
        return self.board.filled

    @property
    def board_empty(self):
        return self.board.empty

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
            move = self.current.turn(self.board)
            if (len(move) == 2 and move in moves):
                break
            os.system('clear')

        self.make_move(move)
        if (self.winning_line()):
            print("stuck")
            self.declare_winner(self.current)
            return

        if self.current == self.p1:
            self.current = self.p2
        else:
            self.current = self.p1

    def make_move(self, move):  # kek
        self.board.place_piece(move, self.current.piece)

    def available_moves(self):
        moves = [m for (m, p) in self.board.pieces.items() if p is " "]
        assert len(moves) == self.board.empty_spaces
        return sorted(moves)

    def occupied_spaces(self):
        spaces = [m for (m, p) in self.board.pieces.items() if p is not " "]
        assert len(spaces) == self.board.occupied_spaces
        return sorted(spaces)

    def display_available_moves(self):
        moves = self.available_moves()
        moves = ", ".join(str(move) for move in moves)
        print("Available moves: {}".format(moves))

    def declare_winner(self, winner):
        self.winner = winner

    def winning_line(self):
        return self.board.calculate_row(
            self.current.piece) or self.board.calculate_column(
            self.current.piece) or self.board.calculate_diag(
            self.current.piece)

    @property
    def game_over(self):
        return self.board_filled or self.winner
