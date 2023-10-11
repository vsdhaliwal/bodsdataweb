from pymongo import MongoClient
import json
import os

def sanction_data_load():
    client = MongoClient('mongodb://88.198.40.216:27017/')
    db = client['sanction'] 

    collection_name_map = {
        'Interval': db['Interval'],
        'Address': db['Address'],
        'Airplane': db['Airplane'],
        'Associate': db['Associate'],
        'BankAccount': db['BankAccount'],
        'LegalEntity': db['LegalEntity'],
        'Company': db['Company'],
        'CryptoWallet': db['CryptoWallet'],
        'Directorship': db['Directorship'],
        'Employment': db['Employment'],
        'Family': db['Family'],
        'Identification': db['Identification'],
        'Membership': db['Membership'],
        'Occupancy': db['Occupancy'],
        'Organization': db['Organization'],
        'Ownership': db['Ownership'],
        'Passport': db['Passport'],
        'Person': db['Person'],
        'Position': db['Position'],
        'Representation': db['Representation'],
        'Sanction': db['Sanction'],
        'Value': db['Value'],
        'Security': db['Security'],
        'UnknownLink': db['UnknownLink'],
        'Vessel': db['Vessel'],
        'Interest': db['Interest'],
        'Asset': db['Asset'],
        'Vehicle': db['Vehicle'],
        'Thing': db['Thing']
    }

    data = []
    with open('./sanction_data/entities.ftm.json', 'r', encoding='utf-8') as file:
        for i, line in enumerate(file, 1):
            temp = json.loads(line)
            data.append(temp)

            schema = temp.get('schema')
            collection = collection_name_map.get(schema)

            if collection is not None:
                collection.insert_one(temp)
                print(f"JSON {i} added.")
            else:
                print(f"Schema '{schema}' is not mapped to any collection.")

    client.close()

    os.remove('./sanction_data/entities.ftm.json')

if __name__ == "__main__":
    sanction_data_load()