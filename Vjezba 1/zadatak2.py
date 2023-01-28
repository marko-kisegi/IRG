import numpy

matrixA = [[1, 1, 1],
           [-1, -2, 1],
           [2, 1, 3]]

matrixB = [6, -2, 13]

# enter 9 numbers for matrix

#for i in range(3):
#    for j in range(3):
#        matrixA[i][j] = int(input())
#    matrixB[i] = int(input())

solution = numpy.linalg.solve(numpy.array(matrixA), numpy.array(matrixB))

print("[ x, y, z] = ", solution)
