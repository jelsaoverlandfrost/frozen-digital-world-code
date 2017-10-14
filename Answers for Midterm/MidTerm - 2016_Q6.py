from copy import deepcopy


def read_func(f):
    input_string = f.read()  # read lines from the file input
    input_list = input_string.split('\n')
    print input_list
    matrix_list = []
    operations_list = []
    output_dict = {}
    split_point = input_list.index('OP')
    matrix_list_string = input_list[1:split_point]
    operations_list_string = input_list[split_point + 1:-1]
    for i in matrix_list_string:
        list_string = i.split()
        int_list = []
        for j in list_string:
            int_list.append(int(j))
        matrix_list.append(int_list)
    for k in operations_list_string:
        list_char = k.split()
        operations_list.append(list_char)
    output_dict = {'matrix': matrix_list, 'op': operations_list}
    return output_dict


def mulRowByC(A, i, c):
    for j in range(len(A[i])):
        A[i][j] *= c
    return A


def addRowMulByC(matOp, i, c, j):
    for k in range(len(matOp[j])):
        matOp[j][k] += matOp[i][k] * c
    return matOp


def gaussElimination(data):
    matrix = deepcopy(data['matrix'])
    operation = data['op']
    for i in operation:
        if i[0] == '1':
            matrix = mulRowByC(matrix, int(i[1]), float(i[2]))
        elif i[0] == '2':
            matrix = addRowMulByC(matrix, int(i[1]), float(i[2]), int(i[3]))
    return data['matrix'], matrix


data = {'matrix': [[2.0, -1.0, 0.0, 1.0, 0.0, 0.0], [-1.0, 2.0, -1.0, 0.0, 1.0, 0.0], [0.0, -1.0, 2.0, 0.0, 0.0, 1.0]],
        'op': [['2', '0', '0.5', '1'], ['1', '1', '0.666666666667'], ['2', '1', '1', '2'], ['1', '2', '0.75'],
               ['2', '2', '0.666666666667', '1'], ['2', '1', '1', '0'], ['1', '0', '0.5']]}
matA, result = gaussElimination(data)
print matA
print result

A = [[0, 2, 1, -1], [0, 0, 3, 1], [0, 0, 0, 0]]
ans = addRowMulByC(A, 0, 0.5, 1)
print ans