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

def get_input_part2(happy_dict_part1):
    keys = list(happy_dict_part1.keys())
    for i in keys:
        happy_dict_part1['me'][i] = 0
        happy_dict_part1[i]['me'] = 0
    return happy_dict_part1
        
ans = 0
def solve(people_lst, n, depth, curr, seated, happy_dict, start = None, solution = 0):
    global ans
    if depth == 1:
        start = curr

    if depth == n:
        ans = max(ans, solution + happy_dict[start][curr] + happy_dict[curr][start])
        return

    for i in people_lst:
        if seated[i]:
            continue
        seated[i] = True
        if depth == 0:
            solve(people_lst, n, depth + 1, i, seated, happy_dict, start, solution)
        else:
            solve(people_lst, n, depth + 1, i, seated, happy_dict, start, solution + happy_dict[i][curr] + happy_dict[curr][i])
        seated[i] = False

    return
        


start = time.time()
happiness_dict = parse_input('input.txt')
people_lst = list(happiness_dict.keys())
seated = {p:False for p in people_lst}
n = len(people_lst)

happiness_dict_part2 = get_input_part2(happiness_dict)
solve(people_lst, n, 0, None, seated, happiness_dict, start = None, solution = 0)
print(ans)

ans = 0
people_lst2 = list(happiness_dict_part2.keys())
seated2 = {p:False for p in people_lst2}
n = len(people_lst2)
solve(people_lst2, n, 0, None, seated2, happiness_dict_part2, start = None, solution = 0)
print(ans)
print('Time: ', time.time() - start)
# if __name__ == '__main__':
#     main()