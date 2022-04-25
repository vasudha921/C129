import csv
data = []
with open ("additionaldata.csv","r") as f:
    csvreader = csv.reader(f)
    for i in csvreader:
        data.append(i)
headers = data[0]
planetdata = data[1:]
for i in planetdata:
    i[2]= i[2].lower()
planetdata.sort(key = lambda planetdata: planetdata[2])
with open ("sorted.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdata)
