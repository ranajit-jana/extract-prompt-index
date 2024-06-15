def collect_unique_entities(api_response):
    unique_entities = set()
    results = api_response.get('results', [])

    for result in results:
        entity_type = result.get('entity_type')
        if entity_type:
            unique_entities.add(entity_type)

    return list(unique_entities)