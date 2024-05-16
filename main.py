from board import Board


def main():
    board = Board(400, 400, 4)

    while board.is_running:
        board.tick()


if __name__ == '__main__':
    main()