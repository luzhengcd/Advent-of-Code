import re
import collections
import time
from functools import lru_cache


def parse_input(input_path):
    happiness_dict = collections.defaultdict(dict)
    with open(input_path) as f:
        for line in f.readlines():
            words = line.split()
            name1 = words[0]
            name2 = words[-1].strip('.')
            if words[2] == 'gain':
                happiness_dict[name1][name2] = int(words[3])
            else:
                happiness_dict[name1][name2] = -int(words[3])
    return happiness_dict


def get_input_part2(dict_part1):
    keys = list(dict_part1.keys())
    for i in keys:
        dict_part1['me'][i] = 0
        dict_part1[i]['me'] = 0
    return dict_part1


def solve(people_lst, seated, happy_dict):
    global ans
    ans = 0
    
    n = len(people_lst)

    @lru_cache(maxsize=None)
    def helper(seated, depth=0, start=None, curr=None, units_so_far=0):
        global ans 

        if depth == n:
            ans = max(ans, units_so_far + happy_dict[start][curr] + happy_dict[curr][start])
            return
            
        for i in people_lst:
            if i not in seated:
                continue
            if depth == 0:
                helper(seated - {i}, depth + 1, i, i, units_so_far)
            else:
                helper(seated - {i}, depth + 1, start, i,
                       units_so_far + happy_dict[i][curr] + happy_dict[curr][i])
        return

    helper(seated)
    return ans


def main():
    # part 1
    dict_part1 = parse_input('input.txt')
    people_lst = list(dict_part1.keys())
    # seated = {p: False for p in people_lst}
    seated = frozenset(people_lst)
    ans1 = solve(people_lst, seated, dict_part1)
    print('Answer for part1: ', ans1)

    # part 2
    dict_part2 = get_input_part2(dict_part1)
    people_lst2 = list(dict_part2.keys())
    # seated2 = {p: False for p in people_lst2}
    seated2 = frozenset(people_lst2)
    ans2 = solve(people_lst2, seated2, dict_part2)
    print('Answer for part2: ', ans2)


if __name__ == '__main__':
    start = time.time()
    main()
    print('Time: ', time.time() - start)
