#multiply matrix

m1 = [[1,2,3],
	  [4,5,6]]

m2 = [[7,8],
	  [9,10],	
	  [11,12]]

m3 = [[0,0],[0,0]]

for i in range(2):
	for j in range(2):
		for k in range(3):
			m3[i][j] += m1[i][k] * m2[k][j]


print(m3)
