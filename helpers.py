import os

def parse_lines(file):
    input_list = []

    for line in file:
        input_list.append(line)
    
    return input_list


def parse_input(path):
    with open(os.path.join('input_data', path), 'r') as file:
        contents = parse_lines(file)
    
    return contents


def stoval(string):
    if string[0] == '+':
        outval = int(string[1:])
    else:
        outval = -1 * int(string[1:])

    return outval
