from Projectile import *

def getInputs():
    a = eval(input('enter the launch angle (in degress): '))
    v = eval(input('enter the initial velocity (in meters/sec): '))
    h = eval(input('enter the initial height (in meters): '))
    t = eval(input('enter the time interval: '))
    return a, v, h, t

def main():
    angle, vel, h0, time = getInputs()
    shot = Projectile(angle, vel, h0)
    while shot.getY() >= 0:
        shot.update(time)
    print('\nDistance traveled:{0:0.1f}meters.'.format(shot.getX()))

if __name__=='__main__':
    main()
    
