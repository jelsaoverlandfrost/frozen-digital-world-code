# submit only part (b)
def f_to_c(fahrenheit):
    """

    :type fahrenheit: float
    """
    c = (fahrenheit - 32) * 5.0 / 9.0
    return c


def f_to_c_approx(fahrenheit):
    c = (fahrenheit - 30) / 2.0
    return c


def get_conversion_table():
    ######Enter your code below ########
    conversion = []  # this is the table mentioned in the questions
    fah = []
    cesaro = []
    celcius = []
    for f in range(0, 101, 10):
        fah.append(f)
        cesaro.append(round(f_to_c(f),1))
        celcius.append(round(f_to_c_approx(f),1))
    conversion.append(fah)
    conversion.append(cesaro)
    conversion.append(celcius)
    ######Ignore code below ############

    return conversion


print get_conversion_table()
