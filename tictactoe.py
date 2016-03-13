#!/usr/bin/python3

import os
import sys
import argparse
from gamestate import GameState
from board import Board


def usage():
    return """Tic Tac Toe"""


def start_game(game_type):
    board = Board()
    p1_name = input("Player 1 enter your name: ")
    if game_type == 'pvp':
        p2_name = input("Player 2 enter your name: ")
        gs = GameState(game_type, board, p1_name, p2_name)
    elif game_type == "ai":
        gs = GameState(game_type, board, p1_name)

    while (not gs.game_over):
        os.system('clear')
        gs.get_next_move()

    os.system('clear')
    gs.build_board()
    print("\nWINNER: {}\n".format(gs.winner))


def main():
    try:
        parser = argparse.ArgumentParser(description=usage(),
                                         epilog="Insert pretentious quote\
                                         about AI from some famous computer\
                                         scientist here",
                                         prog="tictactoe")
        parser.add_argument("-a", action="store_const", dest="game_type",
                            const="ai", help="Artificial Intelligence")
        parser.add_argument("-p", action="store_const", dest="game_type",
                            const="pvp", help="Player versus Player")
        parser.add_argument("-v", action='version', version='%(prog)s 1.0')
        args = parser.parse_args()

        if (len(sys.argv) != 2):
            parser.print_help()
            sys.exit(0)

        start_game(args.game_type)

    except KeyboardInterrupt:
        # os.system('clear')
        sys.exit(0)

if __name__ == '__main__':
    main()
    sys.exit(1)
