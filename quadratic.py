import math

def main() :
    print("this program find the real solutions to a quadratic\n")
    try:
        a, b, c = eval(input("please enter the coefficients (a, b, c): "))
        delta = b * b - 4 * a * c
        discRoot = math.sqrt(delta)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("\nThe solutions are:", root1, root2)
    except ValueError as excObj:
        if str(excObj) == 'math domain error':
            print("No real roots.")
        else:
            print("you didn't give me the right number of coeeficients.")
    except NameError:
        print("\nyou didn't enter three numbers.")
    except TypeError:
        print("\nyour inputs were not all numbers.")
    except SyntaxError:
        print("\nyour input was not in the correct form. Missing comma?")
    except:
        print("\nSomething went wrong, sorry!")
            
main()
