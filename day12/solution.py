import json
import time    
import sys 

def read_input(path):
    with open(path) as f:
        return json.load(f)


SUM_PART1 = 0
def solve_part1(data):
    global SUM_PART1
    if isinstance(data, dict):
        for key, val in data.items():
            solve_part1(key)
            solve_part1(val)
    elif isinstance(data, list):
        for i in data:
             solve_part1(i)
    elif isinstance(data, (int, float)):
        SUM_PART1 += data

    return

def has_red(data):    
    for key, val in data.items():
        if key == 'red' or val == 'red':
            return True
    return False

SUM_PART2 = 0
def solve_part2(data):
    global SUM_PART2
    if isinstance(data, dict):
        if has_red(data):
            return
        for key, val in data.items():
            solve_part2(key)
            solve_part2(val)
    elif isinstance(data, list):
        for i in data:
             solve_part2(i)
    elif isinstance(data, (int, float)):
        SUM_PART2 += data
    return           

def main(path = 'input.txt'):

    data = read_input(path)
    solve_part1(data)
    solve_part2(data)

    print('Answer for part 1: ', SUM_PART1)
    print('Answer for part 2: ', SUM_PART2)

if __name__ == '__main__':
    start = time.time()
    data_path = sys.argv[1]
    main(data_path)
    end = time.time()
    print('Time elapsed: ', end - start)