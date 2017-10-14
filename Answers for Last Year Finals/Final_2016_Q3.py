def maxOccurrence(inputString):
    # Slicing the string to extract the numbers
    charArray = inputString.split()
    # Changing the array to all numbers
    numArray = []
    for i in charArray:
        numArray.append(int(i))
    # Count the occurrence and record it
    recordOccurrence = {}
    for j in range(len(numArray)):
        count = 1
        if numArray[j] not in recordOccurrence.keys():
            for k in range(j + 1, len(numArray)):
                # print recordOccurrence.keys()
                if numArray[j] == numArray[k]:
                    count += 1
        else:
            continue
        if numArray[j] not in recordOccurrence.keys():
            recordOccurrence[numArray[j]] = count
    # Find the maximum occurrence
    maxCount = 0
    for l in recordOccurrence.values():
        if l > maxCount:
            maxCount = l
    # Get the result
    result = []
    for m in recordOccurrence.keys():
        if recordOccurrence[m] == maxCount:
            result.append(m)
    result = sorted(result)
    return result, maxCount


print 'test 1'
inp = '2 3 40 3 5 4 -3 3 3 2 0'
print maxOccurrence(inp)
print 'test 2'
inp = '1 2 3 4 5 6'
print maxOccurrence(inp)
