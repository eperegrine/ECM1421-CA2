"""A module to help locate useful files"""
import os

root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
base_data_path = os.path.join(root_folder, 'data')
crime_data_path = os.path.join(base_data_path, "Devon_and_Cornwall_crime_data_2019")
postcode_file_path = os.path.join(base_data_path, "Devon_postcodes", "postcodes.csv")