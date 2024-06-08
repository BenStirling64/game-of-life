from board import Board
import sys

def main():
    if len(sys.argv) == 1:
        board = Board()
    elif len(sys.argv) == 3:
        try:
            board = Board(width=int(sys.argv[1]), height=int(sys.argv[2]))
        except ValueError:
            print("The width and height must be integer values.")
            return
    elif len(sys.argv) == 4:
        try:
            board = Board(width=int(sys.argv[1]), height=int(sys.argv[2]), zoom=int(sys.argv[3]))
        except ValueError:
            print("The width, height and cell size must be integer values.")
            return
    else:
        print("Usage: python3 main.py <width> <height>")
        return

    while board.is_running:
        board.tick()


if __name__ == '__main__':
    main()