#!/usr/bin/env python3

def part1(ranges):
    total = 0
    for num_range in ranges:
        start = int(num_range[0])
        end = int(num_range[1])

        for num in range(start,end+1):
            str_num = str(num)
            if len(str_num) % 2 != 0: continue
            to_split = int(len(str_num)/2)
            half_1 = str_num[to_split:]
            half_2 = str_num[:to_split]
            if half_1 == half_2: 
                total += num

    print(f'Part1: {total}')

def chunkstring(string, length):
    return [string[i:i+length] for i in range(0, len(string), length)]

def part2(ranges):
    total = 0
    for num_range in ranges:
        start = int(num_range[0])
        end = int(num_range[1])
        for num in range(start,end+1):
            str_num = str(num)
            for i in range(int(len(str_num)/2)):
                num_chunks = chunkstring(str_num, i+1)
                num_sub = num_chunks[0]
                uniform_length = all(len(s) == i+1 for s in num_chunks)
                if not uniform_length: continue 
                repeating_nums = all(s == num_sub for s in num_chunks)
                if repeating_nums: 
                    total += num
                    break

    print(f'Part2: {total}')


def main():
    # with open('test.txt', 'r') as f:
    with open('real.txt', 'r') as f:
        line = f.readlines()[0].strip()
    ranges = line.split(',')
    ranges = [r.split('-') for r in ranges]

    part1(ranges)
    part2(ranges)
    return

if __name__ == '__main__':
    main()
