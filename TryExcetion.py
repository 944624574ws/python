#TryException.py
def main():
    try:
        num1, num2 = eval(input("enter two numbers, separated by a comma"))
        res = num1 / num2
    except ZeroDivisionError:
        print("DIvision by zeros!")
    except SyntaxError:
        print("A comma may be missing in the input")
    except:
        print("No exceptions, the result is", result)
    finally:
        print("executing the final clause")

main()
