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
    pass