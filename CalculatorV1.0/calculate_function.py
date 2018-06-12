def calculator():
    number1 = float(input('Please, enter your first number:'))
    number2 = float(input('Please, enter your second number:'))
    operation = input('Please, enter an operation(choose from: +, -, *, \\):')
    print('Your result is: ' + str(calculate(number1, operation, number2)))

def calculate(number1, operation, number2):
    if operation == '+':
        result = number1 + number2
    elif operation == '-':
        result = number1 - number2
    elif operation == '*':
        result = number1 * number2
    elif operation == '\\':
        if number2 == 0:
            print('Nobody must divide by ziro!')
            return False
        else:
            result = number1 / number2
    else:
        print("Please, enter a correct symbol of an operation.")
        return True
    return result