import input_helpers
import os
import sys

if __name__ == "__main__":
    # String Formatting 
    green = "\033[92m"
    end_text_formatting = '\033[0m'
    underline = '\033[4m'

    print(underline + "STREET CRIME IN DEVON \n" + end_text_formatting + green + "COMMANDS: \n HELP: Outputs An Instructions Document. \n QUIT: Quits The Program. \n RESTART: Restarts The Program. \n" + end_text_formatting)
    postcode = input_helpers.ui_get_postcode()
    
    distance = input_helpers.ui_get_distance()
    sort = input_helpers.ui_get_sort_options()
    output_file = input_helpers.ui_get_file_and_directory()
    

