from board import Board


def main():
    board = Board(1024, 1024)

    while board.is_running:
        board.tick()


if __name__ == '__main__':
    main()