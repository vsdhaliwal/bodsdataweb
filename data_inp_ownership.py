from pymongo import MongoClient
import json

client = MongoClient('mongodb://88.198.40.216:27017/')
db = client['sanction']

def load_sanction_data(files, collection_name_map):

    for filename in files:
        with open(filename, 'r', encoding='utf-8') as file:
            for i, line in enumerate(file, 1):
                data = json.loads(line)
                schema = data.get('statementType')
                collection = collection_name_map.get(schema)

                if collection is not None:
                    collection.insert_one(data)
                    print(f"JSON {i} from {filename} added to {schema} collection.")
                else:
                    print(f"Schema '{schema}' is not mapped to any collection in {filename}.")

    client.close()

if __name__ == "__main__":
    collection_name_map = {
        'entityStatement': db['entity_statement'],
        'ownershipOrControlStatement': db['ownership_or_control_statement'],
        'personStatement': db['person_statement']
    }

    filenames = ['./sanction_data/latvia.json', './sanction_data/another_file.json']
    load_sanction_data(filenames, collection_name_map)
