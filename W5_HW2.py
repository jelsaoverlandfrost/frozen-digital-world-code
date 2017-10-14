def leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def R(y,x):
    return y % x

def day_of_week_jan1(year):
    inner_portion = 1 + 5 * R(year - 1, 4)\
                    + 4 * R(year - 1, 100)\
                    + 6 * R(year - 1, 400)
    day = R(inner_portion, 7)
    return day


def num_days_in_month(month_num,leap_year_judge):
    big_months = [1,3,5,7,8,10,12]
    small_months = [4,6,9,11]
    if month_num in big_months:
        number_of_days = 31
    elif month_num in small_months:
        number_of_days = 30
    else:
        if leap_year_judge:
            number_of_days = 29
        else:
            number_of_days = 28
    return number_of_days

def construct_cal_month(month_num, first_day_of_month, num_days_in_month):
    month_list = []
    month_dict = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
    month_list.append(month_dict[month_num])
    date_counter = 1
    day_counter = first_day_of_month
    week_string = ''
    week_string = week_string + day_counter * '   '
    while date_counter < num_days_in_month + 1:
        while day_counter < 7 and date_counter < num_days_in_month + 1:
            if date_counter < 10:
                week_string = week_string + '  ' + str(date_counter)
            else:
                week_string = week_string + ' ' + str(date_counter)
            day_counter += 1
            date_counter += 1
        month_list.append(week_string)
        week_string = ''
        day_counter = 0
    return month_list

def construct_cal_year(year):
    year_list = []
    year_list.append(year)
    for i in range(1, 13):
        days_passed = 0
        for j in range(1,i):
            days_passed += num_days_in_month(j, leap_year(year))
        day_of_week = (day_of_week_jan1(year) + days_passed) % 7
        this_month = construct_cal_month(i, day_of_week, num_days_in_month(i, leap_year(year)))
        year_list.append(this_month)
    return year_list


def display_calendar(calendar_year, month):
    if month == None:
        year_list = construct_cal_year(calendar_year)
        year_list.pop(0)
        answer_string = ''
        for i in range(len(year_list)):
            for j in range(len(year_list[i])):
                answer_string = answer_string + year_list[i][j] + '\n'
                if j == 0:
                    answer_string = answer_string + '  S  M  T  W  T  F  S\n'
            answer_string = answer_string + '\n'
        answer_string = answer_string[:-2]
        return answer_string
    else:
        days_passed = 0
        for j in range(1, month):
            days_passed += num_days_in_month(j, leap_year(calendar_year))
        day_of_week = (day_of_week_jan1(calendar_year) + days_passed) % 7
        month_list = construct_cal_month(month, day_of_week, num_days_in_month(month, leap_year(calendar_year)))
        answer_string = ''
        for i in range(len(month_list)):
            answer_string += month_list[i] + '\n'
            if i == 0:
                answer_string += '  S  M  T  W  T  F  S\n'
        answer_string = answer_string[:-1]
        return answer_string
'''

def display_calendar(calendar_year):
    year_list = construct_cal_year(calendar_year)
    year_list.pop(0)
    answer_string = ''
    for i in range(len(year_list)):
        for j in range(len(year_list[i])):
            answer_string = answer_string + year_list[i][j] + '\n'
            if j == 0:
                answer_string = answer_string + '  S  M  T  W  T  F  S\n'
        answer_string = answer_string + '\n'
    answer_string = answer_string[:-2]
    return answer_string
'''

print display_calendar(2002,3)