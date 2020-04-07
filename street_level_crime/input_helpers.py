"""A module to help get user input"""
import re
import os
import sys
import postcode as postcode_lookup
from file_resolver import *

uk_postcode_format = re.compile("([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2})")
valid_file_name = re.compile('^[^\\\<>:"/|?]+$')


def validate_postcode(postcode):
    """Returns true if the postcode is a valid EX postcode"""
    return bool(uk_postcode_format.match(postcode)) and postcode[:2].upper() == "EX"


def validate_file_name(file_name):
    """Returns true if the file name is valid and not a path"""
    return bool(valid_file_name.match(file_name))


def ui_get_postcode_and_coordinate():
    """Keeps looping until the user enters a postcode which we can find a coordinate for"""
    while True:
        postcode = get_user_input("Please, enter postcode (e.g. EX4 4QJ) \n")
        if validate_postcode(postcode):
            coord = postcode_lookup.postcode_to_coordinate(postcode_file_path, postcode)
            if coord is not None:
                return postcode, coord
            else:
                print("Your postcode could not be found")
        else:
            print("Please, check your postcode. It must be a valid UK format (e.g. EX4 4QJ)")


def ui_get_distance():
    """Keeps looping until a valid distance is selected"""
    while True:
        distance = get_user_input("Please, select distance from postcode centre: \n [1] 1km \n [2] 2km \n [3] 5km \n")
        if distance in ["1", "2", "3"]:
            return float(distance)
        else:
            print("Please, select a number from 1 to 3")


def ui_get_sort_options():
    """Keeps looping until a valid sort option is selected"""
    while True:
        option = get_user_input("Please, select sort option (number 1 to 3): \n [1] By disatnce from the postcode centre \n [2] By date (most recent first) \n [3] Crime category \n")
        if option in ["1", "2", "3"]:
            return int(option)
        else:
            print("Please, select a number from 1 to 3")


def ui_get_file_and_directory():
    """Keeps looping until a valid file path and name is entered"""
    while True:
        print("A file path example", os.path.expanduser("~"))
        path_to_directory = get_user_input("Please, enter a path to destination folder: ")
        if os.path.isdir(path_to_directory):
            print("Path accepted")
            break
        elif os.path.exists(os.path.join(os.path.dirname(os.getcwd()), path_to_directory)):
            print("Using relative path:", os.path.join(os.path.dirname(os.getcwd()), path_to_directory))
            break
        elif os.path.isdir(os.path.dirname(path_to_directory)):
            try:
                os.mkdir(path_to_directory)
                print("Path not found, New directory created at ", path_to_directory)
                break
            except:
                print("Unable to make directory folder with same name can't exist at path location")
        else:
            print("Path to directory doesn't exist. Please, try again.")

    while True:
        file_name = get_user_input("Please enter a file name: ")
        path_to_file = os.path.join(path_to_directory, file_name)
        path_to_file_ext = path_to_file + ".csv"
        if not os.path.isfile(path_to_file_ext) and validate_file_name(file_name):
            print("File name accepted")
            return path_to_file_ext
        elif os.path.isfile(path_to_file_ext):
            print("File already exists. Please, try different name")
        else:
            print("Wrong! Path cant contain the following characters: < (less than) , > (greater than) , : (colon) , \" (double quote) , / (forward slash)  , \\ (backslash) , | (vertical bar or pipe) \n ? (question mark) , * (asterisk)")


def ui_commands(command_input):
    """Handles running the commands"""
    # String formatting
    green = "\033[92m"
    blue = '\033[94m'
    end_text_formatting = '\033[0m'
    underline = '\033[4m'

    command_input = command_input.upper()
    if command_input == "HELP":
       print( underline + "SYSTEM INSTRUCTIONS:" + end_text_formatting + blue + "\n [1] You will be asked to input a postcode, make sure this is an EX postcode as the program does not accept other areas. \n [2] Then you need to select the distance of crimes you want to display, you will get the option to display crimes in a 1, 2 or 5KM radius (You need to type 1 for 1km, 2 for 2KM or 3 for 5KM.) \n [3] You can then select the way the data is sorted, by distance, date and category of the crime. (You need to type 1 for distance, 2 for date or 3 for category) \n [4] And then you can select where the data will be saved to. This will be a file path located on your computer (e.g. C:\\Users\\Name) \n [5] Finally, you can enter a name that you want the file to be saved as (E.G. Crime_Data,  NOTE: The file name already has the ‘.csv’ extension added) \n Then your file will be saved for you to use." + end_text_formatting)
       print(green + "COMMANDS: \n HELP: Outputs An Instructions Document. \n QUIT: Quits The Program. \n RESTART: Restarts The Program. \n" + end_text_formatting)
    elif command_input == "RESTART":
        raise RestartCommand()
    elif command_input == "QUIT":
        sys.exit(0)
    else:
        print("Command Not Recognised")


def get_user_input(message):
    """An input wrapper to check for commands"""
    while True:

        user_input = input(message)

        commands = ["HELP", "RESTART", "QUIT"]
        if user_input.upper() in commands:
            ui_commands(user_input)
        else:
            return user_input


class RestartCommand(Exception):
    """Exception to allow program to restart"""
    pass
