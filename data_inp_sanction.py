from pymongo import MongoClient
import json

client = MongoClient('mongodb://localhost:27017/')
db = client['your_database'] 

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
with open('temp.json', 'r', encoding='utf-8') as file:
    for line in file:
        temp = json.loads(line)
        data.append(temp)

print(len(temp))

for item in data:
    schema = item['schema']
    collection = collection_name_map.get(schema)

    if collection is not None:
        collection.insert_one(item)
    else:
        print(f"Schema '{schema}' is not mapped to any collection.")

client.close()
