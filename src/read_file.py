import csv

def read_file(filename):
    record = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            record.append(row)
    return record

if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    data = read_file(filename)
    print(data)
