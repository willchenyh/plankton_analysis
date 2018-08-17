import csv
with open('class01_05.csv', 'rb') as inp, open('class01_05_tail.csv', 'wb') as out:
    writer = csv.writer(out)
    for row in csv.reader(inp):
        if row[16] != "Rejected":
            writer.writerow(row)
