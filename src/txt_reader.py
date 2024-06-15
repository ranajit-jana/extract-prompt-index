def read_txt_file(filename):
    record = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            record.append(line.strip())
    return record

if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    data = read_txt_file(filename)
    print(data)
