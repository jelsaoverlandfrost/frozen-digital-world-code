def average_list(inp):
    output = []
    for i in range(len(inp)):
        subsum = 0
        subavg = 0
        for j in range(len(inp[i])):
            subsum += inp[i][j]
        subavg = subsum / len(inp[i])
        output.append(subavg)
    return output

print average_list([[100],[1,7],[8,0,-1],[0]])