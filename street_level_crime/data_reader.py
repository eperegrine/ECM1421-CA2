import csv
import os


def get_csv_files_in_folder(folder_path):
    f = []
    for (dirpath, dirnames, filenames) in os.walk(folder_path):
        csv_files_at_level = []
        for fname in filenames:
            _, ext = os.path.splitext(fname)
            if ext == ".csv":
                csv_files_at_level.append(dirpath + fname)

        f.extend(csv_files_at_level)
    return f

if __name__ == "__main__":
    directory_name = "data"#input("Dir name: ")
    print(get_csv_files_in_folder(directory_name))
    print("\nEND\n")