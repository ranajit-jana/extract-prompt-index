import os
import sys
import hashlib
from read_file import read_file
from make_api_call import make_api_call
from api_call_to_elastic import call_elastic_search

csvfolderlocation = sys.argv[1]
llm_server_url = sys.argv[2]
es_url = sys.argv[3]
es_index = sys.argv[4]
es_category = sys.argv[5]


def process_files(csvfolderlocation, llm_server_url, es_url, es_index, es_category):
    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(current_dir)
    data_dir = os.path.join(parent_dir, csvfolderlocation)
    files = os.listdir(data_dir)

    for file in files:
        csv_file_name = str(os.path.join(data_dir, file))
        print(csv_file_name)
        with open(csv_file_name, newline="\n", encoding="utf-8") as csvfile:
            csvreader = csv.DictReader(csvfile)
            headers = csvreader.fieldnames
            record_number = 0

            for row in csvreader:
                record_number += 1
                for header in headers:
                    if (
                        header.endswith("_id")
                        or header.endswith("timestamp")
                        or header.endswith("count")
                    ):
                        continue
                    data = row[header]
                    print(f"{file},{record_number},{header}: {data}")

                    response_text_data = make_api_call(data, llm_server_url)
                    if response_text_data:
                        entity_types = [
                            obj["entity_type"] for obj in response_text_data
                        ]
                        calculatedid = "".join([file, str(record_number), header, data])
                        positive_hash_value = hashlib.md5(
                            calculatedid.encode()
                        ).hexdigest()
                        for entity in entity_types:
                            response = call_elastic_search(
                                entity,
                                file,
                                record_number,
                                header,
                                es_url,
                                es_index,
                                es_category,
                                positive_hash_value,
                            )
                            print(response)
                            print(entity)
                        print("\n\n\n")


if __name__ == "__main__":
    process_files(csvfolderlocation, llm_server_url, es_url, es_index, es_category)
