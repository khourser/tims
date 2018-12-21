import csv

def csvWR(list2d):
    #f = open('db_.csv', 'wb')
    with open('db_.csv','w') as f:
        csvWriter = csv.writer(f)
        for row in list2d:
            csvWriter.writerow(row)
        f.close()
