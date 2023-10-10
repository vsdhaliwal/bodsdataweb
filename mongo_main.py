from pymongo import MongoClient
from schema_dict import *

client = MongoClient('mongodb://88.198.40.216:27017/')
db = client['sanction']  

interval_collection = db['Interval']
address_collection = db['Address']
airplane_collection = db['Airplane']
associate_collection = db['Associate']
bank_account_collection = db['BankAccount']
legal_entity_collection = db['LegalEntity']
company_collection = db['Company']
crypto_wallet_collection = db['CryptoWallet']
directorship_collection = db['Directorship']
employment_schema_collection = db['Employment']
family_collection = db['Family']
identification_collection = db['Identification']
membership_collection = db['Membership']
occupancy_collection = db['Occupancy']
organization_collection = db['Organization']
ownership_collection = db['Ownership']
passport_collection = db['Passport']
person_collection = db['Person']
position_collection = db['Position']
representation_collection = db['Representation']
sanction_collection = db['Sanction']
value_collection = db['Value']
security_collection = db['Security']
unknown_link_collection = db['UnknownLink']
vessel_collection = db['Vessel']
interest_collection = db['Interest']
asset_collection = db['Asset']
vehicle_collection = db['Vehicle']
thing_collection = db['Thing']

ownership_or_control_statement_schema_collection = db['ownershipOrControlStatement']
entity_statement_schema_collection = db['entityStatement']
person_statement_schema_collection = db['personStatement']

collections_schemas = {
    interval_collection: interval_schema,
    address_collection: address_schema,
    airplane_collection: airplane_schema,
    associate_collection: associate_schema,
    bank_account_collection: bank_account_schema,
    legal_entity_collection: legal_entity_schema,
    company_collection: company_schema,
    crypto_wallet_collection: crypto_wallet_schema,
    directorship_collection: directorship_schema,
    employment_schema_collection: employment_schema,
    family_collection: family_schema,
    identification_collection: identification_schema,
    membership_collection: membership_schema,
    occupancy_collection: occupancy_schema,
    organization_collection: organization_schema,
    ownership_collection: ownership_schema,
    passport_collection: passport_schema,
    person_collection: person_schema,
    position_collection: position_schema,
    representation_collection: representation_schema,
    sanction_collection: sanction_schema,
    value_collection: value_schema,
    security_collection: security_schema,
    unknown_link_collection: unknown_link_schema,
    vessel_collection: vessel_schema,
    interest_collection: interest_schema,
    asset_collection: asset_schema,
    vehicle_collection: vehicle_schema,
    thing_collection: thing_schema,
    ownership_or_control_statement_schema_collection: ownership_or_control_statement_schema,
    entity_statement_schema_collection: entity_statement_schema,
    person_statement_schema_collection: person_statement_schema
}

ownership_or_control_statement = {
    "statementID": "fbfd0547-d0c6-4a00-b559-5c5e91c34f5c",
    "statementType": "ownershipOrControlStatement",
    "isComponent": False,
    "statementDate": "2017-11-18",
    "subject": {
      "describedByEntityStatement": "1dc0e987-5c57-4a1c-b3ad-61353b66a9b7"
    },
    "interestedParty": {
      "describedByPersonStatement": "019a93f1-e470-42e9-957b-03559861b2e2"
    },
    "interests": [
      {
        "type": "shareholding",
        "directOrIndirect": "direct",
        "beneficialOwnershipOrControl": True,
        "startDate": "2016-04-06",
        "share": {
          "exact": 100,
          "minimum": 100,
          "maximum": 100
        }
      }
    ],
    "publicationDetails": {
      "publicationDate": "2018-02-13",
      "bodsVersion": "0.3",
      "publisher": {
        "name": "CHRINON LTD"
      }
    }
  }

entity_statement = {
    "statementID": "1dc0e987-5c57-4a1c-b3ad-61353b66a9b7",
    "statementType": "entityStatement",
    "isComponent": False,
    "statementDate": "2017-11-18",
    "entityType": "registeredEntity",
    "name": "CHRINON LTD",
    "foundingDate": "2010-11-18",
    "identifiers": [
      {
        "scheme": "GB-COH",
        "id": "07444723"
      }
    ],
    "publicationDetails": {
      "publicationDate": "2018-02-13",
      "bodsVersion": "0.3",
      "publisher": {
        "name": "CHRINON LTD"
      }
    }
  }

person_statement = {
    "statementID": "019a93f1-e470-42e9-957b-03559861b2e2",
    "statementType": "personStatement",
    "isComponent": False,
    "statementDate": "2017-11-18",
    "personType": "knownPerson",
    "nationalities": [
      {
        "code": "GB",
        "name": "United Kingdom of Great Britain and Northern Ireland (the)"
      }
    ],
    "names": [
      {
        "type": "individual",
        "fullName": "Christopher Taggart",
        "givenName": "Christopher",
        "familyName": "Taggart"
      },
      {
        "type": "alternative",
        "fullName": "Chris Taggart"
      }
    ],
    "birthDate": "1964-04",
    "addresses": [
      {
        "type": "service",
        "address": "Aston House, Cornwall Avenue, London",
        "country": "GB",
        "postCode": "N3 1LF"
      }
    ],
    "publicationDetails": {
      "publicationDate": "2018-02-13",
      "bodsVersion": "0.3",
      "publisher": {
        "name": "CHRINON LTD"
      }
    }
  }

ownership_or_control_statement_schema_collection.insert_one(ownership_or_control_statement_schema)
entity_statement_schema_collection.insert_one(entity_statement_schema)
person_statement_schema_collection.insert_one(person_statement_schema)
print("Statement schemas inserted successfully.")

for collection, schema in collections_schemas.items():
    if collection.count_documents({}) == 0:
        collection.insert_one(schema)
        print(f"Collection {collection.name} created successfully.")
    else:
        print(f"Collection {collection.name} already contains documents. Skipping insertion.")
