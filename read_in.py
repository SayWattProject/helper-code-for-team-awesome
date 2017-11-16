import csv


def read_csv():
    data = []
    with open('SAMPLE-ADDRESSES-Sheet1-3.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(spamreader, None) #skip header
        for row in spamreader:
            if int(row[2]) == 1:
                location = {}
                location['lat'] = row[0]
                location['lon'] = row[1]
                data.append(location)
    return data
#print main()
