import os
import csv
import requests

from pii_api import pii_detection_call  # Import the function from the new module
from persist_in_pdsa import persist_in_pdsa  # pdsa call
from process_text import process_text_file
from process_csv import process_csv_file
from construct_payload import construct_payload
import uuid

pii_detection_url="http://localhost:8001/analyze/"
pdsa_url="http://localhost:8000/api/pii_identification_record"




def read_files_in_folders(folders):
    run_id = str(uuid.uuid4())
    for folder in folders:
        print(f"Processing folder: {folder}")
        for filename in os.listdir(folder):
            filepath = os.path.join(folder, filename)
            if filename.endswith('.txt'):
                print(f"Processing text file: {filename}")
                txtvar = process_text_file(filepath)
                # Make first API call (PII Detection)
                pii_detection_response = pii_detection_call(pii_detection_url, txtvar)
                if pii_detection_response is not None:

                    #print(f"PII Detection API response: {pii_detection_response}")
                    payload = construct_payload(run_id,"1",filepath,pii_detection_response, "not capturing")
                    # Make second API call (Persist in PDSA)
                    #print(f" Payload Passed \n {payload}")
                    pdsa_response = persist_in_pdsa(pdsa_url, payload)
                    if pdsa_response:
                        print(f"Persist in PDSA API response: {pdsa_response}")
                    else:
                        print("Persist in PDSA API request failed.")
                else:
                    print("PII Detection API request failed.")
            elif filename.endswith('.csv'):
                print(f"Processing CSV file: {filename}")
                csvvar = process_csv_file(filepath)
                pii_detection_response = pii_detection_call(pii_detection_url, txtvar)
                if pii_detection_response:
                    print(f"PII Detection API response: {pii_detection_response}")
                    payload = construct_payload(run_id,1,filepath,pii_detection_response, "not capturing")
                    # Make second API call (Persist in PDSA)
                    pdsa_response = persist_in_pdsa(pdsa_url, payload)
                    if pdsa_response:
                        print(f"Persist in PDSA API response: {pdsa_response}")
                    else:
                        print("Persist in PDSA API request failed.")
                else:
                    print("PII Detection API request failed.")
            else:
                print(f"Ignoring file: {filename} (unsupported format)")

def main():
    # Example folders to process
    folders_to_process = [
        "../credit_card_processing",
        "../generated_files"
    ]

    # folders_to_process = [
    #     "../exploratorydata"
    # ]
    # Read and process files in each specified folder
    read_files_in_folders(folders_to_process)

if __name__ == "__main__":
    main()
