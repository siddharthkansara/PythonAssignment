#add two matrices

m1 = [[1,2],
	 [3,4]]

m2 = [[5,6],
	 [7,8]]

# first way

m3 = [[0,0],[0,0]]

for i in range(2):
	for j in range(2):
		m3[i][j] = m1[i][j] + m2[i][j]

print(m3)


# second way 

m4 = [[m1[i][j] + m2[i][j] for j in range(2)] for i in range(2)]

print(m4)

