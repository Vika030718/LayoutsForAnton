def calculate(number1, operation, number2):
    if operation == '+':
        result = number1 + number2
    elif operation == '-':
        result = number1 - number2
    elif operation == '*':
        result = number1 * number2
    elif operation == '/':
        if number2 == 0:
            print('Nobody must divide by ziro!')
            return False
        else:
            result = number1 / number2
    else:
        print("Please, enter a correct symbol of an operation.")
        return True
    return result
