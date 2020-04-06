import csv
import shutil
import os


def convert_to_csv(headers: tuple, data: list) -> csv:
    """
 Converts variables to csv
    :Tuple headers: Contians the headers of the csv file
    :List data: Contains a list of row data in format List[List[String]]
    """
    print("When entering a filename please don't add .csv to the file")
    filename = input("Please enter a filename: ")
    special_commands(filename)
    try:
        with open(filename + '.csv', 'w+', newline='') as f:  # creates document and opens for writer object
            csvWriter = csv.writer(f)
            csvWriter.writerow(headers)
            for i in range(0, len(data) - 1, 1):
                csvWriter.writerow(data[i])
            print("File Created:", filename + ".csv")
            f.close()
            
            print("Do you want to save to a custom path?")
            print("[1] Yes")
            print("[2] No")
            CustomPathInput = input()
            special_commands(CustomPathInput)
            if CustomPathInput == "1":
                custom_path(filename)
            else:
                print("Saved to default location: " + os.path.dirname(
                    os.path.realpath(filename + ".csv")) + '\\' + filename + ".csv")
    except:
        print("Error writing to CSV")
        csvWriter.writerow("Error writing to CSV")


def custom_path(filename):
    try:
        src = os.path.dirname(os.path.realpath(filename + ".csv")) + '\\' + filename + ".csv"
        home = os.path.expanduser("~")
        dst = home + "\\" + input("Please enter a directory: " + home + "\\")
        special_commands(dst)
        if os.path.exists(dst):
            shutil.move(src, dst)
            print("Saved to: " + dst)
        else:
            print("Saved to default location: " + src)
    except:
        print("Unable to save file to custom path")


def special_commands(variable):
    pass
    # Link to Jack Gittoes' Code


headers = ['a', 'b', 'c']
data = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o']]
convert_to_csv(headers, data)
