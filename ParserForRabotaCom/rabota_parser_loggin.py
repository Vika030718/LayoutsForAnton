import csv

class Logger(object):

    @classmethod
    def log_reader(self):

        with open('rabota_data.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            for line in csv_reader:
                print(line)

    @classmethod
    def log_cleaner(self):

        with open('rabota_data.csv', 'w') as csv_file:
            csv_file.truncate()

    def log_writer(self, data):

        log_row = [data['name'], data['city'], data['description']]

        with open('rabota_data.csv', 'a') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow(log_row)
