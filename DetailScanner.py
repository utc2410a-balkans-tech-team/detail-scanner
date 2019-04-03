import sys
import csv

inputFile = sys.argv[1]

readData = []

with open(inputFile, "r") as f:
    fileReader = csv.reader(f)
    firstRead = True
    for row in fileReader:
        if firstRead == True:
            firstRead = False
            continue
        readData.append(row)

print(readData)
