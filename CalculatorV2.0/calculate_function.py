import csv, datetime

class Logging:

    def log_reader(self):

        with open('calculator_history.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            for line in csv_reader:
                print(line)

    def log_clear(self):

        with open('calculator_history.csv', 'w') as csv_file:
            csv_file.truncate()

class Scanner:

    def __init__(self, user_phrase):
        self.user_phrase = user_phrase

    def log_writer(self, expression, result):

        log_row = [str(datetime.date.today()), expression, result]

        with open('calculator_history.csv', 'a') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow(log_row)

    def set_list(self):
        expression = self.user_phrase.replace(" ", "")
        # Check if there are any unsupported characters in the string
        expression_list = []
        for ch in expression:
            if ch not in '01234567890+-*/.()':
                print('Unsupported Character: ' + ch)
                exit()
            expression_list.append(ch)

        count = 0
        while count < len(expression_list) - 1:
            if expression_list[count].isdigit() and expression_list[count+1].isdigit():
                expression_list[count]+=expression_list[count+1]
                expression_list.pop(count+1)
            else:
                count += 1

        return expression_list

    def calculate(self, number1, operation, number2):
        if operation == '+':
            result = int(number1) + int(number2)
        elif operation == '-':
            result = int(number1) - int(number2)
        elif operation == '*':
            result = int(number1) * int(number2)
        elif operation == '/':
            if int(number2) == 0:
                print('Nobody must divide by ziro!')
                return False
            else:
                result = int(number1) / int(number2)
        else:
            print('Please, enter a correct symbol of an operation.')
            return True
        return result

    def scann(self):
        expression = self.set_list()
        parentheses = ['(', ')']

        while len(expression) != 1:
            count = 0
            while count < len(expression) - 1:
                if expression[count] == "(":
                    if expression[count + 2] == ")":
                        expression.pop(count+2)
                        expression.pop(count)
                count += 1
            # Multiply and divide
            count = 0
            while count < len(expression) - 1:
                if expression[count] in ['*', '/'] and not (expression[count+1] in parentheses or expression[count-1] in parentheses):
                    expression[count - 1] = self.calculate(expression[count - 1], expression[count], expression[count + 1])
                    expression.pop(count+1)
                    expression.pop(count)
                count += 1
            # Add and subtact
            count = 0
            while count < len(expression) - 1:
                if expression[count] in ['+', '-'] and not (expression[count+1] in parentheses or expression[count-1] in parentheses):
                    expression[count - 1] = self.calculate(expression[count - 1], expression[count], expression[count + 1])
                    expression.pop(count+1)
                    expression.pop(count)
                count += 1

        result = expression[0]
        self.log_writer(self.user_phrase, result)

        return result