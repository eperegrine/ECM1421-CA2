import csv

def postcode_to_coordinate(variables_file, postcode):
    postcode = postcode.replace(' ', '').lower()
    file = csv.DictReader(open(variables_file))

    for row in file: 
        if row["Postcode"].replace(' ', '').lower() == postcode: 
            latitude = float(row["ETRS89GD-Lat"])
            longitude = float(row["ETRS89GD-Long"])
            return (latitude, longitude)
    return None

if __name__ == "__main__":
    coordinate = postcode_to_coordinate('data\Devon_postcodes\postcodes.csv', 'DT1 1AA')
    print(coordinate)