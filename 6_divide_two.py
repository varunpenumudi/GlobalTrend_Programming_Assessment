def divide(a, b):
    try:
        res = a / b
        return res
    except ZeroDivisionError:
        return "ERROR: Cannot Divide by Zero"


if __name__ == "__main__":
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print(divide(num1, num2))
