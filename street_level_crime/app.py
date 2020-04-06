import input_helpers
import create_csv
import os
import sys
import postcode
import data_reader

root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
base_data_path = os.path.join(root_folder, 'data')
crime_data_path = os.path.join(base_data_path, "Devon_and_Cornwall_crime_data_2019")
postcode_file_path = os.path.join(base_data_path, "Devon_postcodes", "postcodes.csv")

def main_application():
    # String Formatting
    green = "\033[92m"
    end_text_formatting = '\033[0m'
    underline = '\033[4m'

    print(underline + "STREET CRIME IN DEVON \n" + end_text_formatting + green + "COMMANDS: \n HELP: Outputs An Instructions Document. \n QUIT: Quits The Program. \n RESTART: Restarts The Program. \n" + end_text_formatting)
    user_postcode = input_helpers.ui_get_postcode()

    coordinate = postcode.postcode_to_coordinate(postcode_file_path, user_postcode)
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