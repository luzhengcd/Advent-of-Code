import collections
import string

def parse(path = 'input.txt'):
	replacements = collections.defaultdict(list)
	with open(path) as f:
		for line in f:
			if '=' in line:
				tokens = line.split()
				from_char, to_char = tokens[0], tokens[-1]
				replacements[from_char].append(to_char)
			else:
				start = line.strip()
	return replacements, start

def parse_start(start_str):
	start_lst = []
	upper_letters = set(string.ascii_uppercase)
	prev = None
	for s in start_str:
		if s in upper_letters:
			if prev is not None:
				start_lst.append(prev)
			prev = s
		else:
			start_lst.append(prev + s)
			prev = None
	if prev is not None:
		start_lst.append(prev)
	return start_lst
		

def main():
	replacements, start = parse()
	module_set = set()
	start_lst = parse_start(start)
	for idx, s in enumerate(start_lst):
		for replacement in replacements[s]:
			module_set.add( ''.join(start_lst[:idx] + [replacement] + start_lst[idx + 1 : ]))
	print('Answer for part 1: {}'.format(len(module_set)))

if __name__ == '__main__':
	main()