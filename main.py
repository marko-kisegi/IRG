import numpy as np

a = np.array([2, 3, -4]) 
b = np.array([-1, 4, -1])
v1 = a + b
print("v1 je ", v1)

s = np.dot(v1, np.array([-1, 4, -1]))
print(s)
v2 = np.matmul(v1, np.array([2, 2, 4]))
print(v2)
v3 = np.linalg.norm(v1)
print(v3)
v4 = -v2
print(v4)
help_matrix1 =	np.array([[1, 2 , 3],
		[2, 1, 3],
		[4, 5, 1]])
help_matrix2 =	np.array([[-1, 2, -3],
		[5, -2, 7],
		[-4, -1, 3]])
help_matrix3 =	np.array([[1, 2, 3],
		[2, 1, 3],

		[4, 5, 1]])
help_matrix4 =	np.array([[-1, 2, -3],
		[5, -2, 7],
		[-4, -1, 3]])

temp = help_matrix4.transpose()
M1 = np.matmul(help_matrix1, help_matrix2)
M2 = np.matmul(help_matrix3, temp)
M3 = np.matmul(help_matrix3, np.linalg.inv(help_matrix4))

print(M1)
print(M2)
print(M3)

x = np.array([	[1, 1, 1],
		[-1, -2, 1],
		[2, 1, 3]])
sol = np.array([6, -2, 13])
x = np.linalg.inv(x)
solution = np.dot(x,sol)
print(solution)

matrix = np.array( 	[[1, 6, 11],
			[1, 11, 1],
			[0, 2, 0]])

matrix = np.linalg.inv(matrix)
tocke = np.array( [6, 6, 1])
baricentricne = np.dot(matrix, tocke)

print(baricentricne)
