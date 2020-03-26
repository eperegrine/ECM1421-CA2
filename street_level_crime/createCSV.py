import csv

rowData = []
columnHeaders = []


def convertToCSV(data):
    try:
        rowNumber = 0
        with open('crime data.csv', 'w', newline='') as f:
            csvWritter = csv.writer(f)
            columnHeaders[:] = data[0]
            rowLength = len(columnHeaders[:])
            rowCount = len(data[1]) / rowLength
            data[:] = data[1]
            csvWritter.writerow(columnHeaders)
            try:
                for i in range(1, int(rowCount) + 1, 1):
                    splitRows(data, rowLength, i)
                    csvWritter.writerow(rowData)
                    rowNumber = rowNumber + 1
            except:
                print("Error writing to CSV")
                csvWritter.writerow("Error writing to CSV")
    except:
        print("Data error")


def splitRows(data, rowLength, rowNumber):
    firstPositionInRow = (rowLength * rowNumber) - rowLength
    lastPositionInRow = (rowLength * rowNumber)
    rowData[:] = data[firstPositionInRow:lastPositionInRow]


# Column Headers stored in first array
# Data to be stored in second array
data = [['a', 'b', 'c'], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']]
convertToCSV(data)
