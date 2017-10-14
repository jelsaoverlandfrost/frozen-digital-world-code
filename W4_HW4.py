def most_frequent(numList):
    countList = []
    numberList = []
    finalList = []
    for i in range(len(numList)):
        count = 0
        for j in range(i, len(numList)):
            if numList[j] == numList[i]:
                count += 1
        countList.append(count)
        numberList.append(numList[i])

    for k in range(len(numberList)):
        if countList[k] == max(countList):
            finalList.append(numberList[k])
    return finalList


print most_frequent([9, 30, 3, 9, 3, 2, 4])
