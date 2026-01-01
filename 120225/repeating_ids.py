#!/usr/bin/env python3

def part1(ranges):
    total = 0
    for num_range in ranges:
        start = int(num_range[0])
        end = int(num_range[1])

        # print(f'Range: {start}, {end}')

        for num in range(start,end+1):
            str_num = str(num)
            if len(str_num) % 2 != 0: continue
            to_split = int(len(str_num)/2)
            half_1 = str_num[to_split:]
            half_2 = str_num[:to_split]
            if half_1 == half_2: 
                # print(f'Invalid ID: {num}')
                total += num

    print(f'Part1: {total}')

def main():
    # with open('test.txt', 'r') as f:
    with open('real.txt', 'r') as f:
        line = f.readlines()[0].strip()
    ranges = line.split(',')
    ranges = [r.split('-') for r in ranges]

    part1(ranges)
    return

if __name__ == '__main__':
    main()
