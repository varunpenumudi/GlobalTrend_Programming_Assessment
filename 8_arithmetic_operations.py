def operation(num1, num2, operator):
    if operator not in ["+", "-", "*", "/"]:
        return "ERROR: Not a valid Operator"

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    else:
        return num1 / num2


if __name__ == "__main__":
    num1 = int(input("Enter the firsrt number: "))
    num2 = int(input("Enter the second number: "))
    operator = input("Enter the operator:  ")
    print(operation(num1, num2, operator))
