from math import pi, sin, cos, radians

def main():
    angle = eval(input('enter the launch angle (in degress):'))
    vel = eval(input('enter the initial velocity (in meters/sec):'))
    h0 = eval(input('enter the initial height (in meters):'))
    time = eval(input('enter the time interval: '))

    xpos = 0
    ypos = h0
    theta = radians(angle)
    xvel = vel * cos(theta)
    yvel = vel * sin(theta)

    while ypos >= 0:
        xpos = xpos + time * xvel;
        yvell = yvel - time * 9.8;
        ypos = ypos + time * (yvel + yvell) / 2.0
        yvel = yvell
    print('\nDistance traveled:{0:0.1f}meters.'.format(xpos))

if __name__=='__main__':
    main()
