# Define the function to check if the input is a number or not
def checkDigit(digit):
    try:
        float(digit);
        return True;
    except ValueError:
        pass;

    try:
        import unicodedata
        unicodedata.numeric(digit);
        return True;
    except (TypeError, ValueError):
        pass;


# To make the loop work
i = 0;
for i in range(0, 40):

    person = raw_input("Enter Your Name:");
    studentid = raw_input("Enter Your Student ID:");

    # Get the inputs:

    while 1 == 1:
        quiz = raw_input("Enter Your Mark for Quiz:");
        if not checkDigit(quiz):
            print "Wait... is that a number?";
            continue;
        elif float(quiz) > 100 or float(quiz) < 0:
            print "No Cheating Please =("
        else:
            quiz = float(quiz);
            break;

    while 1 == 1:
        project = raw_input("Enter Your Mark for Project:");
        if checkDigit(project) != True:
            print "Wait... is that a number?";
            continue;
        elif float(project) > 100 or float(project) < 0:
            print "No Cheating Please =("
        else:
            project = float(project);
            break;

    while 1 == 1:
        finalPaper = raw_input("Enter Your Mark for Final Paper:");
        if checkDigit(finalPaper) != True:
            print "Wait... is that a number?";
            continue;
        elif float(finalPaper) > 100 or float(finalPaper) < 0:
            print "No Cheating Please =("
        else:
            finalPaper = float(finalPaper);
            break;
        # Calculate the average
    average = (quiz + project + finalPaper) / 3;

    # Check the grades
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    # Print
    print "Hello", person + ",", "your Student ID is:", studentid + ",", "your average mark is:", average, "your final grade is", grade
