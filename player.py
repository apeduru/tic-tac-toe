#!/usr/bin/python3

from time import sleep


class Player(object):

    def __init__(self, name, piece):
        self.name = name
        self.piece = piece

    def __str__(self):
        return str(self.name)

    def turn(self):
        move = input("{} input a valid move: ".format(self.name))
        return move


class AI(object):

    def __init__(self, game_state, name, piece):
        self.name = name
        self.game_state = game_state
        self.piece = piece

    def __str__(self):
        return str(self.name)

    def turn(self):
        move = input("Computing {} move...: ".format(self.name))
        sleep(2)
        return move

    def minmax(self):
        pass
