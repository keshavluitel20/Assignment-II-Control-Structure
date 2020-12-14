def calculator(num1, get_operator, num2):
    if get_operator == "+":
        result = num1 + num2
        return result
    elif get_operator == "-":
        result = num1 - num2
        return result
    elif get_operator == "/":
        try:
            result = num1 / num2
            return result
        except ZeroDivisionError:
            print("Number can't be divided by zero.")
    elif get_operator == "*":
        result = num1 * num2
        return result
    else:
        return "Invalid operator"


num_1 = input("Enter first number: ")
operator = input("Enter operator: ")
num_2 = input("Enter second number: ")
if num_1.isdigit() and num_2.isdigit():
    num_1 = float(num_1)
    num_2 = float(num_2)
    print(calculator(num_1, operator, num_2))
else:
    print("Please enter valid number")
