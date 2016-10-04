import numpy
def run():
	grid = numpy.zeros((20,20), dtype = numpy.uint64)
	inp = open("in.txt", "r")
	j = 0
	for line in inp:
		print line
		if len(line) > 1:
			line = line.split(" ")
			for i in range(len(line)):
				grid[j][i] = int(line[i])
		j += 1

	m = 0

	for row in range(20):
		for col in range(20):
			for w1 in [-3, 0, 3]:
				for w2 in [-3, 0, 3]:
					if row + w1 >= 0 and row + w1 < 20:
						if col + w2 >= 0 and col + w2 < 20:
							a = grid[row][col]
							for k in range(1,4):
								a = a*grid[row + k * numpy.sign(w1),col + k * numpy.sign(w2)]
							if a > m:
								m = a
	print m
run()
							





