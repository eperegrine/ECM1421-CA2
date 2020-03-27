import re
import os

uk_postcode_format = re.compile("([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2})")
valid_file_name = re.compile('^[^\\\<>:"/|?]+$')

def validate_postcode(postcode):
    return bool(uk_postcode_format.match(postcode))

def validate_file_name(file_name):
    return bool(valid_file_name.match(file_name))

def ui_get_postcode():
    while True:
        postcode = input("Please, enter postcode (e.g. BH12 2ED)")
        if validate_postcode(postcode):
            return postcode
        else:
            print("Please, check your postcode. It must be a valid UK format (e.g. GH12 2ED)")

def ui_get_distance():
    while True:
        distance = input("Please, select distance from postcode centre: [1] 1km \n [2] 2km \n [3] 5km \n")
        if distance in ["1", "2", "3"]:
            return distance
        else:
            print("Please, select a number from 1 to 3")

#Function to retrieve postcode data from \data\Devon_postcodes\postcodes.csv

#Function to calculate centre coordinate of a postcode

#Function to retreieve all crimes within a distance

def ui_get_sort_options():
    while True:
        option = input("Please, select sort option (number 1 to 3): \n 1. By disatnce from the postcode centre \n 2. By date (most recent first) \n 3. Crime category \n")
        if option in ["1", "2", "3"]:
            return option
        else:
            print("Please, select a number from 1 to 3")

def ui_get_file_and_directory():
    while True:
        path_to_directory = input("Please, enter a path to destination folder: ")
        if os.path.isdir(path_to_directory):
            print("Path accepted")
            break
        else:
            print("Path to directory doesn't exist. Please, try again.")
        
    while True:
        file_name = input("Please enter a file name: ")
        path_to_file=os.path.join(path_to_directory, file_name)
        path_to_file_ext = path_to_file + ".csv"
        if not os.path.isfile(path_to_file_ext) and validate_file_name(file_name):
            print("File name accepted")
            return path_to_file_ext
        elif file_exists(path_to_file):
            print("File already exists. Please, try different name")       
        else:
            print("Wrong! Path cant contain the following characters: < (less than) , > (greater than) , : (colon) , \" (double quote) , / (forward slash)  , \\ (backslash) , | (vertical bar or pipe) \n ? (question mark) , * (asterisk)")
        
