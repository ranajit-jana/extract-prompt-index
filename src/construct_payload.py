import hashlib

def construct_payload(job_run_id, record_id, source_file, entity_detected, redacted_text):
    # Calculate block_id as hash of source_file
    block_id = hashlib.sha256(source_file.encode()).hexdigest()

    # Construct payload dictionary
    payload = {
        "case_id": job_run_id,
        "record_id": record_id,
        "source": source_file,
        "block_id": block_id,
        "entity_name": entity_detected,
        "redacted_text": "Not considering for phase 1"
    }
    return payload

# Example usage:
if __name__ == "__main__":
    # Example data
    job_run_id = "unique_id_for_scheduler_job"
    record_id = 1
    source_file = "C:/folder/sometextwithPII.pdf"
    entity_detected = ["PERSON", "DOB", "MOTHER_NAME", "CREDIT_CARD"]
    redacted_text = "Ignore now"
    
    # Construct payload using the function
    payload = construct_payload(job_run_id, record_id, source_file, entity_detected, redacted_text)
    
    # Print or use the payload as needed
    print(payload)
