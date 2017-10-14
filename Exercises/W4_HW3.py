def multiplication_table(N):

    if N <= 0:
        return None
    else:
        output = []
        for i in range(0, N):
            output.append([])
            for j in range(0, N):
                output[i].append((i+ 1)* (j+ 1))
        return output

print multiplication_table(-1)