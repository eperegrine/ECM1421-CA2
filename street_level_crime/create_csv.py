import csv
import shutil
import os
import input_helpers



def convert_to_csv(headers: tuple, data: list) -> csv:
    """
 Converts variables to csv
    :Tuple headers: Contians the headers of the csv file
    :List data: Contains a list of row data in format List[List[String]]
    """
    # input_helpers.ui_get_file_and_directory()
    path_and_filename = input_helpers.ui_get_file_and_directory()
    filename = os.path.basename(path_and_filename)
    try:
        with open(filename, 'w+', newline='') as f:  # creates document and opens for writer object
            csvWriter = csv.writer(f)
            csvWriter.writerow(headers)
            for i in range(0, len(data) - 1, 1):
                csvWriter.writerow(data[i])
            print("File Created:", filename)
            f.close()
            custom_path(filename,path_and_filename)
    except:
        print("Error writing to CSV")
        print("Saved to default location: " + os.path.dirname(
            os.path.realpath(filename + ".csv")) + '\\' + filename + ".csv")


def custom_path(filename,dst):
    src = os.path.dirname(os.path.realpath(filename)) + '\\' + filename
    shutil.move(src, dst)
    print("Saved to: " + dst)

headers = ['a', 'b', 'c']
data = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o']]
convert_to_csv(headers, data)
