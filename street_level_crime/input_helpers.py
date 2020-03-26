import re

uk_postcode_format = re.compile("([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2})")

def validate_postcode(postcode):
    return bool(uk_postcode_format.match(postcode))

def ui_get_postcode():
    while True:
        postcode = input("Please, enter postcode (e.g. BH12 2ED)")
        if validate_postcode(postcode):
            print ("Correct postcode")
        else:
            print("Please, check your postcode. It must be a valid UK format (e.g. GH12 2ED)")
