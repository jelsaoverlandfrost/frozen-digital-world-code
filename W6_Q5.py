
def calculate(f):
    string = f.read()
    print string.split()


score = open('scores.txt')
calculate(score)
