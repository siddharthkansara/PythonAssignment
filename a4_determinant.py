#determinant of a matrix

m = [[1,2],
	 [3,4]]

d = 1 
c = 1

for i in range(2):
	for j in range(2):
		if i == j:
			d *= m[i][j]
		else:
			c *= m[i][j]

print(d-c)

