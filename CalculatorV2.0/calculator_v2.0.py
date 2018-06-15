#!/usr/bin/python3

from calculate_function import Scanner, Logging

def calculator():
    print('\nHello, You are in The World of Numbers, how can I help you? \n')
    print('1. Calculate something for me.\n2. Show me the history.\n3. Clear the history.\n4. Exit.')

    operation = input('Please, make your choice: ')

    if operation=='1':
        result = Scanner(input('Please, enter your expression: ')).scann()
        print('Your result is: ' + str(result))
    elif operation=='2':
        Logging().log_reader()
    elif operation=='3':
        Logging().log_clear()
        print('Your history has been cleaned.')
    elif operation=='4':
        exit()


if __name__ == "__main__":
    calculator()