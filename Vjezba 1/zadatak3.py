import numpy

trianglepeaks = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]
tdot = [0, 0, 0]

#for i in range(3):
#    for j in range(3):
#        trianglepeaks[i][j] = float(input())

print(trianglepeaks)

#for i in range(3):
#    tdot[i] = float(input())
#

print(tdot)

t = numpy.linalg.solve(numpy.array(trianglepeaks), numpy.array(tdot))

print('t1 t2 t3', t)
