import math
import numpy

# Prvi zadatak
# matrica 2,3,-4 + matrica -1 4 -1

vectorA = [ 2, 3, -4]
vectorB = [-1, 4, -1]

def addVectors(vectorA, vectorB):
    v1 = [0, 0, 0]

    for i in range(3):
        v1[i] = vectorA[i] + vectorB[i]

    return v1

#   Drugi zadatak
# s = v1 * ( -1 , 4 , -1 )
vectorC = [-1, 4, -1]


def multipleVectorMultiplication( v1, vectorC):
    s = 0
    for i in range(3):
        s += v1[i] * vectorC[i]
    return s


# Treci zadatak
# Vektorski produkt v2 = v1 x ( 2,2,4)

vectorD = [ 2, 2, 4]


def crossVectorMultiplication(v1,vectorD):
    v2 = [0, 0, 0]
    for i in range(3):
        v2[i] = (v1[(i+1)%3] * vectorD[(i+2)%3] ) - (v1[(i+2)%3] * vectorD[(i+1)%3])
    return v2


# Cetvrti zadatak
# v3 = |v2| , normirani vektor
def normedVector( v2 ):
    v3 = 0
    for i in range(3):
        v3 += v2[i] * v2[i]
    v3 = math.sqrt(v3)
    return v3

# Peti zadatak
# v4 = -v2 , vektor suprotna smjera


def oppositeDirectionVector(v2, x):
    v4 = [ 0, 0, 0]
    for i in range(3):
        v4[i] = x*v2[i]
    return v4


def transponeMatrix(matrix):
    helpMatrix = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            helpMatrix[j][i] = matrix[i][j]
    return helpMatrix


def addmatrix(matricaX,matricaY):
    M1 = []
    for i in range(3):
        M1.append(addVectors(matricaX[i], matricaY[i]))
    return M1


def multiplymatrix(matricaX, matricaY):
    matricaYt = transponeMatrix(matricaY)
    M2 = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            M2[i][j] += (multipleVectorMultiplication(matricaX[i], matricaYt[j]))
    return M2






# Sesti zadatak
# Dvije matrice zbrojiti, zatim dvije pomnoziti valjda
matricaX = [[1, 2, 3],
            [2, 1, 3],
            [4, 5, 1]]
matricaY = [[-1, 2, -3],
            [5, -2, 7],
            [-4, -1, 3]]
v1 = addVectors( vectorA, vectorB)
print('v1 = 2i-3j-4k + (-i+4j-k) =', v1)
s = multipleVectorMultiplication(v1, vectorC)
print('s = v1 * (-i+4j-k) =', s)
v2 = crossVectorMultiplication(v1, vectorD)
print('v2 = v1 x (2i+2j+4k) =', v2)
v3 = normedVector(v2)
print('v3 = |v2| =', v3)
v4 = oppositeDirectionVector(v2, -1)
print('v4 = - v2 =', v4)
M1 = addmatrix(matricaX,matricaY)
print('M1 = ', matricaX, ' + ', matricaY, ' = ', M1)

matricaYt = transponeMatrix(matricaY)
M2 = multiplymatrix(matricaX, matricaYt)
print('M2 = ', matricaX, ' * ', matricaYt, ' ^T = ', M2)
# trebalo bi biti
# -6 22 3
# -9 29 0
#  3 17 -18

inverse = numpy.linalg.inv(matricaY)
M3 = multiplymatrix(matricaX, inverse)
print('M3 = ', matricaX, ' * ', matricaY, '^-1 = ', M3)
