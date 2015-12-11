#averageInFile.py
def average():
    filename = input("input the filename>> ")
    infile = open(filename, 'r')
    sum = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        for xstr in line.split(','):
            sum = sum + eval(xstr)
            count = count + 1
        line = infile.readline()
    print("the average of the numbers is ", sum / count)

average()
