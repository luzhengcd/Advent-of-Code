import copy

def parse_input(path = 'input.txt'):
	data = []
		
	with open(path) as f:
		for line in f:

			data.append(['.'] + list(line.strip()) + ['.'])
	n_cols = len(data[0])
	# pad the grid with .
	data.append(['.' for _ in range(n_cols)])
	data = [['.' for _ in range(n_cols)]] + data
	
	return data


def get_num_on(grid, r, c):
	neighbors = [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1], 
				[r + 1, c + 1], [r + 1, c - 1], [r - 1, c + 1], [r - 1, c -1]]
	return sum(1 for i in neighbors if grid[i[0]][i[1]] == '#')
	
def update_grid(grid, grid_copy):
	
	n_rows = len(grid)
	n_cols = len(grid[0])
	for i in range(1, n_rows - 1):
		for j in range(1, n_cols - 1):
			num_on = get_num_on(grid, i, j)

			if grid[i][j] == '#':
				if num_on != 2 and num_on != 3:
					grid_copy[i][j] = '.'
			else:
				if num_on == 3:
					grid_copy[i][j] = '#'

	return grid_copy
			

def main():
	data = parse_input()
	data_copy = copy.deepcopy(data)
	cnt_on = 0
	for _ in range(100):
		data = update_grid(data, data_copy)
		data_copy = copy.deepcopy(data)
	for i in range(len(data)):
		for j in range(len(data[0])):
			if data[i][j] == '#':
				cnt_on += 1
	print(cnt_on)

if __name__=='__main__':
	main()