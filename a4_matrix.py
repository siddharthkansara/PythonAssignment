#transpose of matrix

m = [[1,2],
	 [3,4],
	 [5,6]]

print(list(zip(*m)))



print([[ m[row][col] for row in range(3)] for col in range(2)])


