import csv
import shutil
import os
import input_helpers


def convert_to_csv(data: list) -> csv:
    """
 Converts variables to csv
    :Tuple headers: Contians the headers of the csv file
    :List data: Contains a list of row data in format List[List[String]]
    """
    path_and_filename = input_helpers.ui_get_file_and_directory()
    filename = os.path.basename(path_and_filename)
    try:
        with open(filename, 'w+', newline='') as f:  # creates document and opens for writer object
            csvWriter = csv.writer(f)
            for row in data:
                csvWriter.writerow(row)
            print("File Created:", filename)
            f.close()
            custom_path(filename, path_and_filename)
    except:
        print("Error writing to CSV")
        print("Saved to default location: " + os.path.dirname(
            os.path.realpath(filename + ".csv")) + '\\' + filename + ".csv")


def custom_path(filename, dst):
    src = os.path.dirname(os.path.realpath(filename)) + '\\' + filename
    shutil.move(src, dst)
    print("Saved to: " + dst)
