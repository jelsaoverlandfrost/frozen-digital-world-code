def extract_values(values):
    value_list = values.split(' ')
    value1, value2 = value_list[0], value_list[1]
    return (int(value1), int(value2))

def calc_ratios(values):
    value1, value2 = values
    if value2 == 0:
        return None
    else:
        return float(value1) / float(value2)

print calc_ratios('134 289')