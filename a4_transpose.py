#transpose of matrix

m = [[1,2],
	 [3,4],
	 [5,6]]

print(list(zip(*m))) #using zip



print([[ m[i][j] for i in range(3)] for j in range(2)]) #using list comprehension


