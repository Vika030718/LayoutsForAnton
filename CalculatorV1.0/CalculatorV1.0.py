from CalculateFunction import calculate

number1 = input('Please, enter your first number:')
number2 = input('Please, enter your second number:')
operation = raw_input('Please, enter an operation(choose from: +, -, *, \\):')
print('Your result is: ' + str(calculate(number1, operation, number2)))

