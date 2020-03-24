import csv
rowData = []

def convertToCSV(data, rowCount,rowLength):
    rowNumber = 2
    with open('crime data.csv','w', newline='') as f:
        csvWritter = csv.writer(f)
        headers = data[0:rowLength]
        csvWritter.writerow(headers)
        try:
            for i in range (1,rowCount+1,1):
                splitRows(data, rowLength, i)
                csvWritter.writerow(rowData)
                rowNumber = rowNumber + 1
        except:
            pass
            
def splitRows(data, rowLength, rowNumber):
    firstPositionInRow = rowLength*rowNumber
    lastPositionInRow = rowLength*(rowNumber+1)
    rowData[:]= data[firstPositionInRow:lastPositionInRow]



data = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
rowCount = 4
rowLength = 3
convertToCSV(data, rowCount, rowLength)