from pymongo import MongoClient
from schema_dict import *

client = MongoClient('mongodb://localhost:27017/')
db = client['sanction']  

interval_collection = db['interval']
address_collection = db['address']
airplane_collection = db['airplane']
associate_collection = db['associate']
bank_account_collection = db['bank_account']
legal_entity_collection = db['legal_entity']
company_collection = db['company']
crypto_wallet_collection = db['crypto_wallet']
directorship_collection = db['directorship']
employment_schema_collection = db['employment_schema']
family_collection = db['family']
identification_collection = db['identification']
membership_collection = db['membership']
occupancy_collection = db['occupancy']
organization_collection = db['organization']
ownership_collection = db['ownership']
passport_collection = db['passport']
person_collection = db['person']
position_collection = db['position']
representation_collection = db['representation']
sanction_collection = db['sanction']
value_collection = db['value']
security_collection = db['security']
unknown_link_collection = db['unknown_link']
vessel_collection = db['vessel']
interest_collection = db['interest']
asset_collection = db['asset']
vehicle_collection = db['vehicle']
thing_collection = db['thing']

interest_collection.insert_one(interest_schema)
address_collection.insert_one(address_schema)
airplane_collection.insert_one(airplane_schema)
associate_collection.insert_one(associate_schema)
bank_account_collection.insert_one(bank_account_schema)
legal_entity_collection.insert_one(legal_entity_schema)
company_collection.insert_one(company_schema)
crypto_wallet_collection.insert_one(crypto_wallet_schema)
directorship_collection.insert_one(directorship_schema)
employment_schema_collection.insert_one(employment_schema)
family_collection.insert_one(family_schema)
identification_collection.insert_one(identification_schema)
membership_collection.insert_one(membership_schema)
occupancy_collection.insert_one(occupancy_schema)
organization_collection.insert_one(organization_schema)
ownership_collection.insert_one(ownership_schema)
passport_collection.insert_one(passport_schema)
person_collection.insert_one(person_schema)
position_collection.insert_one(position_schema)
representation_collection.insert_one(representation_schema)
sanction_collection.insert_one(sanction_schema)
value_collection.insert_one(value_schema)
security_collection.insert_one(security_schema)
unknown_link_collection.insert_one(unknown_link_schema)
vessel_collection.insert_one(vessel_schema)
asset_collection.insert_one(asset_schema)
vehicle_collection.insert_one(vehicle_schema)
thing_collection.insert_one(thing_schema)




# interval_schema, 
# address_schema, 
# airplane_schema,
# associate_schema,
# bank_account_schema,
# legal_entity_schema,
# company_schema,
# crypto_wallet_schema,
# directorship_schema, 
# employment_schema, 
# family_schema, 
# identification_schema, 
# membership_schema, 
# occupancy_schema,
# organization_schema,
# ownership_schema,
# passport_schema,
# person_schema,
# position_schema,
# representation_schema,
# sanction_schema,
# value_schema,
# security_schema,
# unknown_link_schema,
# vessel_schema,
# interest_schema,
# asset_schema,
# vehicle_schema,
# thing_schema, 