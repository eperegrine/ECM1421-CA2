import csv


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
        with open(filename + '.csv', 'w', newline='') as f:  # creates document and opens for writer object
            csvWriter = csv.writer(f)  # creates writer object
            csvWriter.writerow(headers)  # writes header
            for i in range(0, len(data) - 1, 1):  # writes each row in array
                csvWriter.writerow(data[i])  # writes from
            print("File Created:", filename + ".csv")
            f.close()
    except:
        print("Error writing to CSV")
        csvWriter.writerow("Error writing to CSV")


def special_commands(variable):
    if variable == "q" or "h" or "r" or "quit" or "help" or "restart":
        quit_help_restart_function()


headers = ['a', 'b', 'c']
data = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o']]
convert_to_csv(headers, data)
