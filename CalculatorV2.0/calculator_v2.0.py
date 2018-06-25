#!/usr/bin/python3

from calculate_function import Scanner, Logger

def calculator():
    print('\nHello, You are in The World of Numbers, how can I help you? \n')
    print('1. Calculate something for me.\n2. Show me the history.\n3. Clear the history.\n4. Exit.')

    operation = input('Please, make your choice: ')

    if operation=='1':
        expression = input('Please, enter your expression: ')
        result = Scanner(expression).scann()
        print('Your result is: ' + str(result))
    elif operation=='2':
        Logger.log_reader()
    elif operation=='3':
        Logger.log_cleaner()
        print('Your history has been cleaned.')
    elif operation=='4':
        exit()


if __name__ == "__main__":
    calculator()