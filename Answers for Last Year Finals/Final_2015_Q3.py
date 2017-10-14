def compTrace(matrix):
    traceValue = 0
    for i in range(len(matrix)):
        traceValue += matrix[i][i]
    return traceValue


A = [[2.2, 2, 3.1], [4, 5, 6], [7, 8, 9]]
print compTrace(A)
