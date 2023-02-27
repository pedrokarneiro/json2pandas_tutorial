###################################################################################################
# Pandas convert JSON into a DataFrame
# 4. Flattening nested list and dict from JSON object
# Source: https://towardsdatascience.com/how-to-convert-json-into-a-pandas-dataframe-100b2ae1e0d8
###################################################################################################
import pandas as pd
import json

# nested_mix.json has:
# a common unnamed dictionary (key: value pairs):
#      "school_name": "local primary school",
#      "class": "Year 1",
# 
# with another named dictionary inside it: info (and another one inside (contacts)):
#     "info": {
#        "president": "John Kasich",
#        "address": "ABC road, London, UK",
#        "contacts": {
#            "email": "admin@e.com",
#            "tel": "123456789"
#        }
# 
# and then a plus a named list (students) of unnamed dictionaries:
#    "students": [
#    {
#         "id": "A001",
#         "name": "Tom",
#         "math": 60,
#         "physics": 66,
#         "chemistry": 61
#     },
#     {...},
#     ...
#     ]
# }

# df = pd.read_json('nested_mix.json')
# print(df)
## This will cause a cumbersome situation...
## ValueError: Mixing dicts with non-Series may lead to ambiguous ordering.

# load data using Python JSON module
with open('nested_mix.json','r') as f:
    data = json.loads(f.read())
    
# Normalizing data
# data = the json text
# record_path = [the list of dictionaries in the json text]
df = pd.json_normalize(data, record_path =['students'])
print(df)

# Normalizing data more...
# data = the json text
# record_path = [the list of dictionaries in the json text]
# meta = [the named dictionary root keys as values and sub dictionaries keys as lists]
df = pd.json_normalize(
    data, 
    record_path =['students'], 
    meta=[
        'class',
        ['info', 'president'], 
        ['info', 'contacts', 'tel']
    ]
)
print(df)

