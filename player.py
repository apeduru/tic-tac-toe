#!/usr/bin/python3

import time
from copy import deepcopy
import random


class Player(object):

    def __init__(self, name, piece):
        self.name = name
        self.piece = piece

    def __str__(self):
        return str(self.name)

    def turn(self, board):
        move = input("{} input a valid move: ".format(self.name))
        return move


class AI(object):

    def __init__(self, board, name, piece):
        self.name = name
        self.piece = piece
        self.best_moves = []

    def __str__(self):
        return str(self.name)

    def turn(self, board):
        print("Computing AI move...")
        b = board

        if (b.empty):
            # Useless to consider the algorithm on an empty board,
            # wisely choose one of the four corners
            # proven to have better outcomes than any other space on the board
            best_move = random.choice(["TL", "TR", "BL", "BR"])
            return best_move

        ai_flag = True
        del self.best_moves[:]
        best = self.minmax(ai_flag, b, self.piece)
        best_move = self.analyze_winning_routes()
        print(best[1])
        time.sleep(2)
        return best[1]

    def analyze_winning_routes(self):
        best_moves = list(set(self.best_moves))
        print(best_moves)
        return best_moves

    def make_possible_move(self, b, move, piece):
        b = deepcopy(b)
        b.place_piece(move, piece)
        return b

    def minmax(self, aif, b, piece):
        # the game is won
        if (b.calculate_row(piece) or b.calculate_column(piece) or b.calculate_diag(piece)):
            if (aif):
                return (1, None)
            else:
                return (-1, None)
        elif (b.filled):
            return (0, None)

        moves = b.available_moves()
        # Compute the max term if it is AI turn
        if (aif):
            for move in moves:
                best = (2, None)
                b = self.make_possible_move(b, move, "O")
                value = self.minmax(not aif, b, "X")[0]
                if value <= best[0]:
                    best = (value, move)
                    self.best_moves.append(best)
            return best

        # Compute the min term if it is not AI turn
        else:
            for move in moves:
                best = (-2, None)
                b = self.make_possible_move(b, move, "X")
                value = self.minmax(not aif, b, "O")[0]
                if value >= best[0]:
                    best = (value, move)
            return best
