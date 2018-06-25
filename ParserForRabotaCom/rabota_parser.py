#!/usr/bin/python3

import time
from rabota_parser_function import parser
from rabota_parser_loggin import Logger

def rabota_parser():
    print('1. Parse rabota.com.\n2. Show me the history.\n3. Clear the history.\n4. Exit.')

    operation = input('Please, make your choice: ')

    if operation=='1':
        parser("python")
        time.sleep(5)
    elif operation=='2':
        Logger.log_reader()
    elif operation=='3':
        Logger.log_cleaner()
        print('Your history has been cleaned.')
    elif operation=='4':
        exit()


if __name__ == "__main__":
    rabota_parser()