from board import Board


def main():
    board = Board(1600, 800, 4)

    while board.is_running:
        board.tick()


if __name__ == '__main__':
    main()