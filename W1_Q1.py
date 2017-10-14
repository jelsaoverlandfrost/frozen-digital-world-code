person = raw_input("Enter Your Name:");
studentid = raw_input("Enter Your Student ID:");
quiz = float(raw_input("Enter Your Mark for Quiz:"));
project = float(raw_input("Enter Your Mark for Project:"));
finalPaper = float(raw_input("Enter Your Mark for Final Paper:"));
average = (quiz + project + finalPaper) / 3;
if average >= 50:
    status = "pass";
else:
    status = "fail";
print "Hello", person+"," , "your Student ID is:", studentid+"," , "your final status is", status;