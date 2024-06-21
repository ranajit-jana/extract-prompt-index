import os
import csv
import requests
from datetime import datetime
from pii_api import pii_detection_call  # Import the function from the new module
from persist_in_pdsa import persist_in_pdsa  # pdsa call
from process_text import process_text_file
from process_csv import process_csv_file
from construct_payload import construct_payload
import uuid
import argparse
import socket
import hashlib

pii_detection_url = "http://localhost:8001/analyze/"
pdsa_url = "http://localhost:8000/api/pii_identification_record"


def read_files_in_folders(folders, job_name):
    run_id = str(uuid.uuid4())
    # Determine job name
    if not job_name:
        hostname = socket.gethostname()
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        job_name = f"{hostname}_{current_time}"
    else:
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        job_name = f"{job_name}_{current_time}"

    print(f"Job Name: {job_name}")

    # I want to accept one entry from command line here
    for folder in folders:
        print(f"Processing folder: {folder}")
        for filename in os.listdir(folder):
            filepath = os.path.join(folder, filename)
            if filename.endswith(".txt"):
                print(f"Processing text file: {filename}")
                md5_hash = hashlib.md5()
                md5_hash.update(filename.encode("utf-8"))
                block_hash = md5_hash.hexdigest()
                txtvar = process_text_file(filepath)
                # Make first API call (PII Detection)
                pii_detection_response = pii_detection_call(pii_detection_url, txtvar)
                if pii_detection_response is not None:

                    # print(f"PII Detection API response: {pii_detection_response}")
                    payload = construct_payload(
                        "1",
                        block_hash,
                        run_id,
                        job_name,
                        filepath,
                        pii_detection_response,
                        "not capturing",
                    )
                    # Make second API call (Persist in PDSA)
                    # print(f" Payload Passed \n {payload}")
                    pdsa_response = persist_in_pdsa(pdsa_url, payload)
                    if pdsa_response:
                        print(f"Persist in PDSA API response: {pdsa_response}")
                    else:
                        print("Persist in PDSA API request failed.")
                else:
                    print("PII Detection API request failed.")
            elif filename.endswith(".csv"):
                print(f"Processing CSV file: {filename}")
                md5_hash = hashlib.md5()
                md5_hash.update(filename.encode("utf-8"))
                block_hash = md5_hash.hexdigest()
                csvvar = process_csv_file(filepath)
                pii_detection_response = pii_detection_call(pii_detection_url, txtvar)
                if pii_detection_response:
                    print(f"PII Detection API response: {pii_detection_response}")
                    payload = construct_payload(
                        "1",
                        block_hash,
                        run_id,
                        job_name,
                        filepath,
                        pii_detection_response,
                        "not capturing",
                    )
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

    parser = argparse.ArgumentParser(description="Process some folders.")
    parser.add_argument("job_name", type=str, help="Enter Name of the job")

    args = parser.parse_args()

    # Example folders to process
    folders_to_process = ["../credit_card_processing", "../generated_files"]

    read_files_in_folders(folders_to_process, args.job_name)


if __name__ == "__main__":
    main()

    # folders_to_process = [
    #     "../exploratorydata"
    # ]
    # Read and process files in each specified folder
