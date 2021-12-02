filename = 'input'
depth_increases = 0

with open(filename, 'r') as input_file:
	lines = input_file.readlines()

	previous_sum = 0
	for i in range(0, len(lines) - 2):
		a = int(lines[i])
		b = int(lines[i+1])
		c = int(lines[i+2])
		window_sum = a + b + c

		if window_sum > previous_sum and previous_sum != 0:
			depth_increases += 1

		previous_sum = window_sum

print(f'{depth_increases} depth increases.')
