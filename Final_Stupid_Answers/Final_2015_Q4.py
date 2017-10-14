def findKey(dInput, strInput):
    listOutput = []
    for i in dInput:
        if dInput[i] == strInput:
            listOutput.append(i)
    listOutput = sorted(listOutput)
    return listOutput

dInput = {1:'singapore', 20:'china', 4:'japan', 5:'china', 10:'japan'}
print findKey(dInput, 'china')
print findKey(dInput, 'korea')