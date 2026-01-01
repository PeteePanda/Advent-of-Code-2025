#!/usr/bin/env python 3

def part1(turns, start):
    clicks = 0
    code = start
    for turn in turns:
        c = 1
        if turn < 0: c = -1
        code += turn

        while code > 100 or code < 0:
            code = code+(c*-1*100)
        
        if code == 0 or code == 100:
            code %= 100
            clicks += 1

    print(f"Part 1: {clicks}")
    return

def part2(turns, start):
    clicks = 0
    code = start

    for turn in turns:
        c = 1
        if turn < 0: c = -1

        for _ in range(abs(turn)):
            code += c*1

            if code == 0 or code == 100:
                clicks += 1

            if code > 100 or code < 0:
                code %= 100

    print(f"Part2: {clicks}")
    return

def main():
    with open('code.txt', 'r') as f:
    # with open('test.txt', 'r') as f:
        turns = [int(line.replace('L','-').replace('R','').strip()) for line in f.readlines()]

    part1(turns, 50)
    part2(turns, 50)
    return


if __name__ == '__main__':
    main()
