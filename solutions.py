import helpers
import os

def puzzle1():
    contents = helpers.parse_input('day1.txt')
    run_total = 0

    for line in contents:
        run_total += helpers.stoval(line)

    return str(run_total)

def puzzle2():
    contents = helpers.parse_input('day1.txt')
    prior = set()
    run_total = 0
    index = 0

    while (True):
        run_total += helpers.stoval(contents[index])

        if run_total in prior:
            return str(run_total)
        else:
            prior.add(run_total)
        index += 1

        if index >= len(contents):
            index = 0
