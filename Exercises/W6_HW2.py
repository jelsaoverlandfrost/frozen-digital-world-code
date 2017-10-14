def uncompressed(s):
    i = 1
    answer_string = ''
    while i < len(s):
        answer_string += int(s[i - 1]) * s[i]
        i += 2
    return answer_string

print uncompressed('2a5b1c')