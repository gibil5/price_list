import csv

my_list = []

with open('file.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        my_list.append(myClass(row[0], row[1], row[2:]))