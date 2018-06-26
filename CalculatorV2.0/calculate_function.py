"""Scann and Calculate expressions like (22+33)*2+(11+2)/2"""
import csv
import datetime
import re

class Logger(object):
    """Show and clean Log"""

    @classmethod
    def log_reader(cls):
        """Show Log"""

        with open('calculator_history.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            for line in csv_reader:
                print(line)

    @classmethod
    def log_cleaner(cls):
        """Clean Log"""

        with open('calculator_history.csv', 'w') as csv_file:
            csv_file.truncate()

class Scanner(object):
    """Main class, that scans and calculates the expression"""

    def __init__(self, user_phrase):
        """Init prase"""
        self.user_phrase = user_phrase

    @classmethod
    def log_writer(cls, expression, result):
        """Write log"""

        log_row = [datetime.date.today().strftime("%x"), expression, result]

        with open('calculator_history.csv', 'a') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow(log_row)

    def set_list(self):
        """Set List"""
        expression = self.user_phrase.replace(" ", "")

        # Check if there are any unsupported characters in the string
        expression_list = []
        if re.search('[^0-9+*/.()-]', expression):
            print('Unsupported Character: ')
            exit()
        else:
            for symbol in expression:
                expression_list.append(symbol)

        count = 0
        for _item in expression_list:
            if count < len(expression_list) - 1:
                if expression_list[count].isdigit() and expression_list[count+1].isdigit():
                    expression_list[count] += expression_list[count+1]
                    expression_list.pop(count+1)
                else:
                    count += 1

        return expression_list

    @classmethod
    def calculate(cls, number1, operation, number2):
        """Calculate two digits"""

        if operation == '+':
            result = float(number1) + float(number2)
        elif operation == '-':
            result = float(number1) - float(number2)
        elif operation == '*':
            result = float(number1) * float(number2)
        elif operation == '/':
            if float(number2) == 0:
                print('Nobody must divide by ziro!')
                return False
            else:
                result = float(number1) / float(number2)
        else:
            print('Please, enter a correct symbol of an operation.')
            return True
        return result

    def calculate_subexpression(self, expression):
        """Calculate subexpression"""

        while len(expression) != 1:
            # Multiply and divide
            count = 0
            while count < len(expression) - 1:
                if expression[count] in ['*', '/']:
                    expression[count-1] = self.calculate(expression[count-1], expression[count], expression[count+1])
                    expression.pop(count+1)
                    expression.pop(count)
                count += 1
            # Add and subtact
            count = 0
            while count < len(expression) - 1:
                if expression[count] in ['+', '-']:
                    expression[count-1] = self.calculate(expression[count-1], expression[count], expression[count+1])
                    expression.pop(count+1)
                    expression.pop(count)
                count += 1

        return expression[0]

    def calculate_expression(self, expression):
        """Calculate expression"""

        for counter, value in enumerate(expression):
            if value == "(":

                subexpression = []

                for item in expression[counter+1:]:
                    if item != ")":
                        subexpression.append(item)
                    elif item == ")":
                        break

                expression_len = len(subexpression)
                result = self.calculate_subexpression(subexpression)
                expression[counter] = str(result)

                for _num in range(counter+1, counter+1+expression_len+1):
                    expression.pop(counter+1)

        result = self.calculate_subexpression(expression)

        return result

    def scann(self):
        """Main fanction that gets, scanns and calculate the expression"""

        expression = self.set_list()
        result = self.calculate_expression(expression)
        self.log_writer(self.user_phrase, result)

        return result
