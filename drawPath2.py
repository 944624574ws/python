from turtle import *

def main():
    setup(800, 600, 0, 0)

    color('red')
    width(5)
    shape('turtle')
    speed(5)

    result = []
    file = open('data.txt', 'r')
    for line in file:
        result.append(list(map(float, line.split(','))))
    print(result)

    for i in range(len(result)):
        color((result[i][3], result[i][4], result[i][5]))
        forward(result[i][0])
        if result[i][1]:
            rt(result[i][2])
        else:
            lt(result[i][2])
    goto(0, 0)

if __name__ == '__main__':
    main()
