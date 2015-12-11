#prime.py
import math
def main():
    for n in range(2, 101):
        for x in range(2, int(math.sqrt(n)) + 1):
            if n % x == 0:
                #print(n, 'equals', x, '*', n//x)
                break
        else:
            print(n)

main()
