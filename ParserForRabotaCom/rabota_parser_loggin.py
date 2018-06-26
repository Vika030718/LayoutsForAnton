import csv

class Logger(object):

    @classmethod
    def log_reader(cls):

        with open('rabota_data.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            for line in csv_reader:
                print(line)

    @classmethod
    def log_cleaner(cls):

        with open('rabota_data.csv', 'w') as csv_file:
            csv_file.truncate()

    @classmethod
    def log_writer(cls, data):

        log_row = [data['name'], data['city'], data['description']]

        with open('rabota_data.csv', 'a') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow(log_row)
