import csv

with open('students.txt', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        if int(row[2])<30:
            print(row[0],row[1],row[4])
            
