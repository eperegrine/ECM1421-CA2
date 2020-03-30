import csv


def convert_to_csv(headers: tuple, data: list) -> csv:
    """
 Converts variables to csv
    :Tuple headers: Contians the headers of the csv file
    :List data: Contains a list of row data in format List[List[String]]
    """
    try:
        with open('crime data.csv', 'w', newline='') as f:  # creates document and opens for writer object
            csvWriter = csv.writer(f)  # creates writer object
            csvWriter.writerow(headers)  # writes header
            for i in range(0, len(data) - 1, 1):  # writes each row in array
                csvWriter.writerow(data[i])  # writes from

    except:
        print("Error writing to CSV")
        csvWriter.writerow("Error writing to CSV")
