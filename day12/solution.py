import json

def read_input(path):
    with open(path) as f:
        return json.load(f)


SUM = 0
def solve_part1(data):
    global SUM
    if isinstance(data, dict):
        for key, val in data.items():
            solve_part1(key)
            solve_part1(val)
    elif isinstance(data, list):
        for i in data:
             solve_part1(i)
    elif isinstance(data, (int, float)):
        SUM += data

    return

# SUM_PART2 = 0
def solve_part2(data, local_sum, d):
    global SUM_PART2
        
    if data == 'red' and d == 1:
        return False, local_sum

    if isinstance(data, dict):
        local_sum = 0
        for key, val in data.items():
            has_red1, updated_local_sum = solve_part2(key, local_sum, d + 1)
            has_red2, updated_local_sum = solve_part2(val, local_sum, d + 1)
            print(key, val)
            print(has_red1, has_red2)
            if not has_red1 and not has_red2:
                continue
            else:
                SUM_PART2 -= updated_local_sum
                break
    elif isinstance(data, list):
        for i in data:
            _, _ = solve_part2(i, 0, d + 1)
    elif isinstance(data, (int, float)):
        print('test lst')
        local_sum += data
        SUM_PART2 += data

    return  True, local_sum

SUM_PART2 = 0
data = {"d":"d","e":[1,2,3,4],"f":5}
# data = read_input('input.txt')
solve_part2(data, 0, 0)
print(SUM_PART2)