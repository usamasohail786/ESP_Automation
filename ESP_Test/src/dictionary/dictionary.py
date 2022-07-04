import json

class Dictionary_json:
    # some JSON:
    dictionary_data = '{"company_title": "ESP"}'
    # parse x:
    data = json.loads(dictionary_data)
