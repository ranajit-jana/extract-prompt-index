

# Example function to process CSV file
def process_csv_file(filepath):
    # Function to process a CSV file according to specified logic
    print(f"Processing CSV file: {filepath}")
    with open(filepath, newline='\n', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)
        headers = csvreader.fieldnames
        record_number = 0
        
        for row in csvreader:
            result = []
            record_number += 1
            for header in headers:
                if header.endswith('_id') or header.endswith('timestamp') or header.endswith('count'):
                    continue
                data = row[header].strip()  # Access data for the current header                
                result.append(data)
            fullstring = " \t".join(result)
            # print(f"Processing CSV file: {fullstring}")
    return fullstring
