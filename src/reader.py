import csv
import os
import sys
import requests
import json

csvfolderlocation = sys.argv[1]
llm_server_url = sys.argv[2]
print(csvfolderlocation)
print(llm_server_url)
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
    #   print(file)
    #   filedata = read_file(os.path.join(data_dir,  file))
    #   print(filedata)
      csv_file_name = str(os.path.join(data_dir,  file))
      print(csv_file_name)
      with open(csv_file_name, newline='\n', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        csvreader = csv.DictReader(csvfile)

        # Get the header names
        headers = csvreader.fieldnames
        # Skip the header row if present
        #next(csvreader)
        record_number = 0

        # Iterate over each row in the CSV file
        for row in csvreader:
          record_number += 1
          # Process each row (record)
          #print(row)  # O
          for header in headers:
            if header.endswith('_id'):
              continue
            if header.endswith('timestamp'):
              continue
            if header.endswith('count'):
              continue
            # Access the data for each header
            data = row[header]
            # Process the data as needed
            print(f"{file},{record_number},{header}: {data}")

            # Create a dictionary with the text data
            json_data = {"text": data}

            # Convert the dictionary to a JSON string
            json_string = json.dumps(json_data)
            data = {
                "text": data,
                "key2": "value2"
            }
            print(data)
            try:
                # Make the POST request
                response = requests.post(llm_server_url, json=data)
                if response.status_code == 200:
                  print(f"Record {file},{record_number},{header}: {data} = sent successfully:\n {response.text} \n\n")
                else:
                  print(f"Error sending record {file},{record_number},{header}: {data}: {response.status_code}")
            except Exception as e:
              print(f"An error occurred: {e}")