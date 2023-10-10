# from schema_dict import *



# print(interval_schema, 
#                         address_schema, 
#                         airplane_schema,
#                         associate_schema,
#                         bank_account_schema,
#                         legal_entity_schema,
#                         company_schema,
#                         crypto_wallet_schema,
#                         directorship_schema, 
#                         employment_schema, 
#                         family_schema, 
#                         identification_schema, 
#                         membership_schema, 
#                         occupancy_schema,
#                         organization_schema,
#                         ownership_schema,
#                         passport_schema,
#                         person_schema,
#                         position_schema,
#                         representation_schema,
#                         sanction_schema,
#                         value_schema,
#                         security_schema,
#                         unknown_link_schema,
#                         vessel_schema,
#                         interest_schema,
#                         asset_schema,
#                         vehicle_schema,
#                         thing_schema, )


import json

# Read JSON from a file
temp = []
with open('temp.json', 'r', encoding='utf-8') as file:
    for line in file:
        data = json.loads(line)
        temp.append(data)

print(len(temp))