import requests

def call_ta_persist(entity, file, record_number,
                    header, ta_url, ta_index, ta_category, 
                    positive_hash_value_str):
    ecdata = {
        "entity": entity,
        "file": file,
        "record_number": record_number,
        "header": header
    }
    requests.packages.urllib3.disable_warnings()
    ecresponse = requests.post("/".join([ta_url, ta_index,
                                         ta_category, 
                                         positive_hash_value_str]),
                               verify=False, json=tadata)
    return taresponse.text

if __name__ == "__main__":
    import sys
    entity = sys.argv[1]
    file = sys.argv[2]
    record_number = int(sys.argv[3])
    header = sys.argv[4]
    es_url = sys.argv[5]
    es_index = sys.argv[6]
    es_category = sys.argv[7]
    positive_hash_value_str = sys.argv[8]
    response = call_elastic_search(entity, file, record_number, header, es_url, es_index, es_category, positive_hash_value_str)
    print(response)
