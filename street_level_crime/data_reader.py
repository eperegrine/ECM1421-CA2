import csv
import os
import geodist

from typing import List, Tuple, Any
from enum import IntEnum


class CrimeDataField(IntEnum):
    CrimeID = 0
    Month = 1
    ReportedBy = 2
    FallsWithin = 3
    Longitude = 4
    Latitude = 5
    Location = 6
    LSOAcode = 7
    LSOAname = 8
    CrimeType = 9
    LastOutcomeCategory = 10
    Context = 11


amount_of_crime_data_fields = len(CrimeDataField)


class InvalidCrimeFileError(Exception):
    pass


# Define Types for Aiding Readabilty
CrimeDataRow = List[Any]
CrimeDataFileData = List[CrimeDataRow]
CrimeDataFile = Tuple[List[str], CrimeDataFileData]


def process_crime_line(row: List[str]) -> CrimeDataRow:
    """Takes a list of strings and changes the types to match the crime file structure
    
    Arguments:
        row {List[str]} -- The row to process
    
    Raises:
        InvalidCrimeFileError: The row passed in is not a valid crime data row
    
    Returns:
        CrimeDataRow -- List[str, str, str, str, float, float, str, str, str, str, str, str]
    """
    if len(row) != amount_of_crime_data_fields: raise InvalidCrimeFileError("Row is not the right length")

    for index, value in enumerate(row):
        if index in [CrimeDataField.Longitude, CrimeDataField.Latitude]:
            if (not value): continue  # Value is empty so skip
            try:
                row[index] = float(value)
            except ValueError as err:
                field_type = CrimeDataField(index)
                raise InvalidCrimeFileError(field_type.name + " (" + value + ") should be a float") from err
    return row


def read_crime_csv(filepath: str) -> CrimeDataFile:
    """
    Reads a file, ensures it is a crime data file, and returns a list of the data
    
    Arguments:
        filepath {str} -- The path to the csv file
    
    Returns:
        Tuple[List[str], List[List[str]]] -- the csv headers, then the csv data
    """
    with open(filepath, newline='') as csvfile:
        crime_data_reader = csv.DictReader(csvfile)

        if len(crime_data_reader.fieldnames) != amount_of_crime_data_fields:
            # This check could be made better, but the number of fields is a simple check
            raise InvalidCrimeFileError("File is not a crime file")

        data = []

        for row in crime_data_reader:
            processed = process_crime_line(list(row.values()))
            data.append(processed)

        return crime_data_reader.fieldnames, data


def order_crime_data(crime_data: CrimeDataFileData, field: int, reverse=False) -> CrimeDataFileData:
    """Order the crime data
    
    Arguments:
        crime_data {CrimeDataFileData} -- The data to order
        field {int} -- The field to order by, can be a CrimeDataField value
    
    Keyword Arguments:
        reverse {bool} -- whether or not to reverse the order (default: {False})
    
    Returns:
        CrimeDataFileData -- The ordered crime data file
    """
    return sorted(crime_data, key=lambda x: x[field], reverse=reverse)


def get_csv_files_in_folder(folder_path: str) -> List[str]:
    """Gets all the csv files in the specified directory and its' subdirectories
    
    Arguments:
        folder_path {str} -- The directory to search on
    
    Returns:
        List[str] -- A list of the file paths
    """
    f = []
    for (dir_path, dir_names, file_names) in os.walk(folder_path):
        csv_files_at_level = []
        for file_name in file_names:
            _, ext = os.path.splitext(file_name)
            if ext == ".csv":
                csv_files_at_level.append(
                    os.path.join(dir_path, file_name)
                )

        f.extend(csv_files_at_level)
    return f


def get_crime_in_area(crime_data_directory, centre_coordinate, radius, sort_mode):
    csv_files = get_csv_files_in_folder(crime_data_directory)
    crime_in_radius = []
    crime_header = None
    for csv_file in csv_files:
        header, data = read_crime_csv(csv_file)

        if crime_header == None:
            crime_header = header

        for crime_row in data:
            lat = crime_row[CrimeDataField.Latitude]
            lng = crime_row[CrimeDataField.Longitude]
            if not lat or not lng:
                # If location info is unavailable skip
                continue
            crime_coord = (lat, lng)
            distance = geodist.distance(centre_coordinate, crime_coord)
            if distance <= radius:
                # Add distance to allow sorting by distance without recalculating it
                crime_row.append(distance)
                crime_in_radius.append(crime_row)

    crime_header.append("Distance")

    """
    Sorting 
    1 = distance
    2 = date
    3 = category
    """
    if sort_mode in [1, 2, 3]:
        sorting_key = [
            len(crime_header) - 1,  # Distance is the last key
            CrimeDataField.Month,
            CrimeDataField.CrimeType
        ][sort_mode-1]
        reverse_order = sort_mode == 2
        crime_in_radius = order_crime_data(crime_in_radius, sorting_key, reverse_order)
    else:
        print("Sort Mode not recognised, using default order")

    return crime_header, crime_in_radius


if __name__ == "__main__":
    # TODO: Remove as here for testing
    directory_name = "/Users/emilyperegrine/Documents/Uni/ECM1421_SystemsDevelopment1/CA2/" \
                     "ECM1421-CA2/data/Devon_and_Cornwall_crime_data_2019"  # input("Dir name: ")
    csv_files = get_csv_files_in_folder(directory_name)
    print(csv_files)
    print("=======")
    crime_csv_to_test = csv_files[0]
    print("Crime csv: %s" % crime_csv_to_test)
    header, data = read_crime_csv(crime_csv_to_test)
    print("======")
    line_to_check = data[0]
    print("Processing line {0}".format(line_to_check))
    print(process_crime_line(line_to_check))
    print("=====")
    print("Ordering csv by Location")
    o_data = order_crime_data(data, CrimeDataField.Location, True)
    output = ', '.join(header) + '\n'
    for row in o_data[:10]:
        output += ', '.join(str(i) for i in row) + os.linesep
    print(output)

    print("\nEND\n")
