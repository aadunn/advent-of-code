filename = 'input'
depth_increases = 0

with open(filename, 'r') as input_file:
	lines = input_file.readlines()

	previous_depth = -1
	for line in lines:
		current_depth = int(line)
		if current_depth > previous_depth and previous_depth != -1:
			depth_increases += 1

		previous_depth = current_depth

print(f'{depth_increases} depth increases.')
