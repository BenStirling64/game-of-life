def argument_parser(arg_list):
    board_properties = {}

    for i in range(1, len(arg_list), 2):
        if arg_list[i] == '--help':
            board_properties['send_help'] = True
            break
        elif arg_list[i] in ('-w', '--width'):
            board_properties['width'] = int(arg_list[i + 1])
        elif arg_list[i] in ('-h', '--height'):
            board_properties['height'] = int(arg_list[i + 1])
        elif arg_list[i] in ('-c', '--cell-size'):
            board_properties['cell_size'] = int(arg_list[i + 1])
        elif arg_list[i] in ('-f', '--frame-rate'):
            board_properties['frame_rate'] = int(arg_list[i + 1])

    return board_properties

def print_help():
    print("Welcome to Conway's Game of Life!\nBy default, the board has 400x200 cells (over a 1600x800 window), and each cell is 4x4 pixels large.\nThe simulation targets a frame rate of 60 frames per second.\n\nThe options are as follows:\n'-w <width>' or '--width <width>' changes the width of the window to <width> pixels\n'-h <height>' or '--height <height>' changes the height of the window to <height> pixels\n'-c <cell_size>' or '--cell-size <cell_size>' changes the size of each cell to <cell_size>x<cell_size> pixels.\n'-f <fps>' or '--frame-rate <fps>' forces the simulation to target <fps> frames per second.")