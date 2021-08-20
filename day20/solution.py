import math
from collections import defaultdict

def solve_part1(num_presents):
    house_num = 1
    num_present_per_house = 0
    
    while num_present_per_house < num_presents:
        num_present_per_house = 0 
        half_way = math.ceil(math.sqrt(house_num))
        for elf in range(1, half_way):
            if house_num % elf== 0:
                num_present_per_house += (elf * 10 + house_num / elf * 10)
        if half_way ** 2 == house_num:
            num_present_per_house += half_way * 10
        house_num += 1
        
    return house_num - 1

def solve_part2(target):
    # have a dictionary to track how many times the elf has delivered
    elf_tracker = defaultdict(int)
    house_num = 1
    num_present_per_house = 0
    
    while num_present_per_house < target:
        num_present_per_house = 0 
        half_way = math.ceil(math.sqrt(house_num))

        for elf in range(math.ceil(house_num / 50), half_way):
            if elf_tracker.get(elf, 0) < 50:
                if house_num % elf== 0:
                    num_present_per_house += (elf * 11 + house_num / elf * 11)
                elf_tracker[elf] += 1
            else:
                continue
        if half_way ** 2 == house_num:
            num_present_per_house += half_way * 11
        house_num += 1
        
    return house_num - 1 

def main():
    target = 33100000
    lowest_house_num = solve_part1(target)
    # PART 2 TAKES FOREVER, DO NOT RUN
    lowest_house_num2 = solve_part2(target)
    print('answer for part 2: {}'.format(lowest_house_num2))

if __name__ == '__main__':
    main()