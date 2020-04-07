import input_helpers
import create_csv
import os
import sys
import postcode
import data_reader
from file_resolver import *

def main_application():
    # String Formatting
    green = "\033[92m"
    end_text_formatting = '\033[0m'
    underline = '\033[4m'

    print(underline + "STREET CRIME IN DEVON \n" + end_text_formatting + green + "COMMANDS: \n HELP: Outputs An Instructions Document. \n QUIT: Quits The Program. \n RESTART: Restarts The Program. \n" + end_text_formatting)
    postcode, coordinate = input_helpers.ui_get_postcode_and_coordinate()
    print(coordinate)

    distance = input_helpers.ui_get_distance()
    sort = input_helpers.ui_get_sort_options()

    header, c_data = data_reader.get_crime_in_area(crime_data_path, coordinate, distance, sort)
    print(str(len(c_data)) + " crimes found")

    path = input_helpers.ui_get_file_and_directory()
    data_with_header = [header]
    data_with_header.extend(c_data)

    create_csv.convert_to_csv(data_with_header, path)

if __name__ == "__main__":
    while True:
        try:
            main_application()
            break
        except input_helpers.RestartCommand:
            red = '\033[91m'
            bold = '\033[1m'
            end_text_formatting = '\033[0m'
            print(red + bold + " \n RESTARTING PROGRAM \n" + end_text_formatting)