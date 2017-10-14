from quizB_others import sum_of_double_even_place, get_size, get_prefix

def is_valid(number):
    if (sum_of_double_even_place(number) + sum_of_odd_place(number)) % 10 == 0:
        return True
    else:
        return False

def get_digit(number):
    if number < 10:
        return number
    else:
        return int(str(number)[0]) + int(str(number)[1])

def sum_of_odd_place(number):
    submision = 0
    for i in range(1,get_size(number),2):
        submision += int(str(number)[i])
        print str(number)[i]
    return submision

def prefix_matched(number, d):
    if int(str(number)[0]) == d:
        return True
    else:
        return False

print sum_of_odd_place(4388576018402626)