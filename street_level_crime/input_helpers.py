import re

uk_postcode_format = re.compile("([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2})")
valid_file_name = re.compile('[^\\\<>:"/|?*]')

def validate_postcode(postcode):
    return bool(uk_postcode_format.match(postcode))

def validate_file_name(file_name):
    return bool(valid_file_name.match(file_name))

def ui_get_postcode():
    while True:
        postcode = input("Please, enter postcode (e.g. BH12 2ED)")
        if validate_postcode(postcode):
            break
        else:
            print("Please, check your postcode. It must be a valid UK format (e.g. GH12 2ED)")

def ui_get_distance():
    while True:
        distance = input("Please, select distance from postcode centre: [1] 1km \n [2] 2km \n [3] 5km \n")
        if distance in ["1", "2", "3"]:
            break
        else:
            print("Please, select a number from 1 to 3")
        return distance

#Function to retrieve postcode data from \data\Devon_postcodes\postcodes.csv

#Function to calculate centre coordinate of a postcode

#Function to retreieve all crimes within a distance

def ui_get_sort_options():
    while True:
        option = input("Please, select sort option (number 1 to 3): \n 1. By disatnce from the postcode centre \n 2. By date (most recent first) \n 3. Crime category \n")
        if option == str(1) or option == str(2) or option == str(3):
            break
        else:
            print("Please, select a number from 1 to 3")
    return option

def ui_get_file_name():
    while True:
        file_name = input("Please enter a file name for report")
        if validate_file_name(file_name):
            print("File name accepted")
            return file_name
        else:
            print("Wrong! Path cant contain the following characters: < (less than) , > (greater than) , : (colon) , \" (double quote) , / (forward slash)  , \\ (backslash) , | (vertical bar or pipe) \n ? (question mark) , * (asterisk)")

def ui_get_directory_name():
    while True:
        directory_name = input("Please, enter a path to destination folder")
        if validate_file_name(directory_name):
            print("Path accepted")
            return directory_name
        else:
            print("Wrong! Path cant contain the following characters: < (less than) , > (greater than) , : (colon) , \" (double quote) , / (forward slash)  , \\ (backslash) , | (vertical bar or pipe) \n ? (question mark) , * (asterisk) ")

        
#Function to produce a tabular report
