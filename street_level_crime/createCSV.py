import csv
def convertToCSV(data, rowCount,columnHeaders):
    with open('a.csv','w', newline='') as f:
        csvWritter = csv.writer(f)

        csvWritter.writerow(columnHeaders)
        for i in range (1,rowCount,1):
            splitRows()
            csvWritter.writerow(rowData)

def splitRows(data, rowNumber, rowLength):

    return rowData