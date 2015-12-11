#average.py
def average():
    xstr = input("enter a nubmer>> ")
    sum = 0
    count = 0
    while xstr != "":
        x = eval(xstr)
        sum = sum + x
        count = count + 1
        xstr = input("enter a number>> ")
    print("the average is ", sum/count)

average()
