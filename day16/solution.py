import re
import sys

def parse_input(input_path = 'input.txt'):
	pattern = re.compile(r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)')
	
	with open(input_path) as f:
		for line in f:
			aunt_idx, compound1, val1, compound2, val2, compound3, val3 = re.match(pattern, line).groups()
			yield aunt_idx, {compound1: int(val1), compound2: int(val2), compound3: int(val3)}

def solve_part1(data):
	reference = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 
		     'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 
		     'perfumes': 1}
	for aunt_idx, aunt_info in data:
		flag = True
		for key in aunt_info.keys():
			if aunt_info[key] == reference[key]:
				continue
			else:
				flag = False
				break
		if flag:
			return aunt_idx

def main():
	if len(sys.argv) < 2:
        	data = parse_input()
	else:
        	data = parse_input(sys.argv[-1])
	
	print(solve_part1(data))
	

if __name__ == '__main__':
	main()