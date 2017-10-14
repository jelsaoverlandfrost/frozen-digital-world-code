def interlock(word1, word2, word3):
    check = True
    if len(word1) + len(word2) != len(word3):
        check = False
    else:
        for i in word1:
            if i not in word3:
                check = False
        for j in word2:
            if j not in word3:
                check = False
        if len(word1) == len(word2) == len(word3) == 0:
            check = False
    return check


print interlock('', '', '')
