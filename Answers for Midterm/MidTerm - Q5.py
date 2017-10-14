#### This problem will be graded manually.
#### Please ignore the points given out by Tutor.

def get_students(students, course):
    name_list = []
    for i in range(len(students)):
        if course in students[i][1]:
            name_list.append(students[i][0])
    return name_list


# As stated in question, use the following list to test your solution.
students = [("Alan", ["CompSci", "Physics", "Math"]),
            ("Justin", ["Math", "CompSci", "Stats"]),
            ("Edward", ["CompSci", "Philosophy", "Economics"]),
            ("Margaret", ["InfSys", "Accounting", "Economics", "CommLaw"]),
            ("Philip", ["Sociology", "Economics", "Law", "Stats", "Music"]),
            ("Mary", ["Math", "CompSci", "Stats"]),
            ("Vera", ["CompSci", "Philosophy", "Economics"]),
            ("Mike", ["InfSys", "Accounting", "Economics", "CommLaw"]),
            ("Donna", ["Sociology", "Economics", "Law", "Stats"])]

print get_students(students, 'History')