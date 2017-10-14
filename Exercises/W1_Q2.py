person = raw_input("Enter Your Name:");
studentid = raw_input("Enter Your Student ID:");
quiz = float(raw_input("Enter Your Mark for Quiz:"));
project = float(raw_input("Enter Your Mark for Project:"));
finalPaper = float(raw_input("Enter Your Mark for Final Paper:"));
average = (quiz + project + finalPaper) / 3;
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
print "Hello", person+"," , "your Student ID is:", studentid+"," , "your average mark is:", average, "your final grade is", grade;