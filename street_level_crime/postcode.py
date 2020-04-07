"""A module to get the coordinates of a postocde"""
import csv

def postcode_to_coordinate(variables_file, postcode):
    postcode = postcode.replace(' ', '').lower()

    with open(variables_file) as file:
        csvfile = csv.DictReader(file)

        for row in csvfile:
            if row["Postcode"].replace(' ', '').lower() == postcode:
                latitude = float(row["ETRS89GD-Lat"])
                longitude = float(row["ETRS89GD-Long"])
                return (latitude, longitude)
        return None

if __name__ == "__main__":
    coordinate = postcode_to_coordinate('data/Devon_postcodes/postcodes.csv', 'EX4 4QJ')
    print(coordinate)