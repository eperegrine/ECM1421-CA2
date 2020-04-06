import csv
import shutil
import os


def convert_to_csv(data: list, path_and_filename: str) -> csv:
    """
 Converts variables to csv
    :List data: Contains a list of row data in format List[List[String]]
    :String Path: Contians the headers of the csv file
    """
    filename = os.path.basename(path_and_filename)
    try:
        with open(path_and_filename, 'w+', newline='') as f:  # creates document and opens for writer object
            csvWriter = csv.writer(f)
            for row in data:
                csvWriter.writerow(row)
            print("File Created:", filename)
            f.close()
    except:
        print("Error writing to CSV")
        dirname = os.path.dirname(os.path.realpath(filename + ".csv"))
        print("Saved to default location: " + os.path.join(dirname, filename + ".csv"))

