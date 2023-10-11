from pymongo import MongoClient
import json
import os

def load_ownership_data(files):
    client = MongoClient('mongodb://88.198.40.216:27017/')
    db = client['sanction']

    collection_name_map = {
        'entityStatement': db['entity_statement'],
        'ownershipOrControlStatement': db['ownership_or_control_statement'],
        'personStatement': db['person_statement']
    }

    for filename in files:
        with open(filename, 'r', encoding='utf-8') as file:
            for i, line in enumerate(file, 0):
                data_list = json.loads(line)
                for data in data_list:
                    schema = data.get('statementType')

                    if schema is not None:
                        collection = collection_name_map.get(schema)
                        if collection is not None:
                            collection.insert_one(data)
                            print(f"JSON added from {filename} added to {schema} collection.")
                        else:
                            print(f"Schema '{schema}' is not mapped to any collection in {filename}.")
                    else:
                        print(f"Could not find 'statementType' in {filename}. Skipping line {i}.")

    client.close()

    for filename in files:
        os.remove(filename)
