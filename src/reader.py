import csv
import os
import sys


csvfolderlocation = sys.argv[1]
print(csvfolderlocation)

def read_file(filename):
    record = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            record.append(row)
    return record


if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(current_dir)
    data_dir = os.path.join(parent_dir, csvfolderlocation)
    files = os.listdir(data_dir)
    for file in files:
      print(file)
      filedata = read_file(os.path.join(data_dir,  file))
      print(filedata)
