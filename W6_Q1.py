def reverse(s):
    answer_string = ''
    for i in range(0, len(s)):
        answer_string += s[len(s) - i - 1]
    return answer_string
