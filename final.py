import csv
data1 = []
data2 = []

with open ("data.csv", "r") as f:
    csvreader = csv.reader(f)
    for i in csvreader:
        data1.append(i)
headers1 = data1[0]
planetdata1 = data1[1:]

with open ("sorted.csv", "r")as f:
    csvreader = csv.reader(f)
    for i in csvreader:
        data2.append(i)
headers2 = data2[0]
planetdata2 = data2[1:]

headers = headers1+ headers2
planetdata = []
for index, i in enumerate(data1):
    planetdata.append(data1[index]+data2[index])

with open ("final.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdata)






