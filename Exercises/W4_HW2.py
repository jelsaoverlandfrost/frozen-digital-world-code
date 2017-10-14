def max_list(inp):
    maximum = []
    for i in range(len(inp)):
        submax = -10000
        for j in range(len(inp[i])):
            if inp[i][j] > submax:
                submax = inp[i][j]
        maximum.append(submax)
    return maximum

inlist = [[1 ,2 ,3] ,[4 ,5] ,[32 ,3 ,4]]
print max_list(inlist)