import csv
matrix = []
f = open('./db_.csv', 'r')
csvReader = csv.reader(f)
for row in csvReader:
    matrix.append(row)
    print(row)
f.close()
