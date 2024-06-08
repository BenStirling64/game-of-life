from board import Board
from utils import argument_parser, print_help
import sys

def main():
    args = argument_parser(sys.argv)

    if args.get('send_help'):
        print()
        print_help()
        return

    board = Board(args)

    while board.is_running:
        board.tick()


if __name__ == '__main__':
    main()