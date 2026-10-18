# Creating a CSV and printing it:
import csv

header = ['NAMES:']
names = [['Bob'], ['James'], ['Alica'], ['Mark'], ['Sam'], ['Sara']]

with open('names.csv', 'w', newline = '') as file:

    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(names)

with open('names.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)