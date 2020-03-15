import re

uk_postcode_format = re.compile("([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2})")
correct_postcode = False

while not correct_postcode:

    postcode = input("Please, enter postcode (e.g. BH12 2ED)")

    if bool(uk_postcode_format.match(postcode)):
        print ("Correct postcode")
        correct_postcode = True

    else:
        print("Please, check your postcode. It must be a valid UK format (e.g. GH12 2ED)")
