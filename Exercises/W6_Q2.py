def check_password(password):
    check_indicator = True
    digit_number = 0
    if len(password) < 8:
        check_indicator = False
    else:
        for i in range(len(password)):
            if password[i].isdigit():
                digit_number += 1
            elif password[i].isalpha():
                continue
            else:
                check_indicator = False
                break
        if digit_number < 2:
            check_indicator = False
    return check_indicator