import csv

rowData = []
columnHeaders = []


def new_convert_to_csv(headers: tuple, data: list) -> csv:
    """
 Converts variables to csv
    :Tuple headers: Contians the headers of the csv file
    :List data: Contains a list of row data in format List[List[String]]
    """
    try:
        rowNumber = 0
        with open('crime data.csv', 'w', newline='') as f:
            csvWriter = csv.writer(f)
            csvWriter.writerow(headers)

            for i in range(0, len(data) - 1, 1):
                csvWriter.writerow(data[i])

    except:
        print("Error writing to CSV")
        csvWriter.writerow("Error writing to CSV")