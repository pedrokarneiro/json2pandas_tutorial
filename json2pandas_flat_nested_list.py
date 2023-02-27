###################################################################################################
# Pandas convert JSON into a DataFrame
# 3. Flattening nested list from JSON object
# Source: https://towardsdatascience.com/how-to-convert-json-into-a-pandas-dataframe-100b2ae1e0d8
###################################################################################################
import pandas as pd
import json

# This will show the dataframe with the column students as a nested list.
df = pd.read_json('data/nested_list.json')
print('The original dataframe df \'as is\' from the json file:')
print(df)

# load data using Python JSON module
with open('data/nested_list.json','r') as f:
    data = json.loads(f.read())
    
# Flatten data with pd.json_normalize(). Give data read (the json string) and the nested list column.
df_nested_list = pd.json_normalize(data, record_path =['students'])
print('\nThe column students (before a dictionary) now as a separate dataframe:')
print(df_nested_list)

# The df_nested_list created is a Pandas dataframe.
print(type(df_nested_list))

# This will include school_name and class (from df)
flat_df = pd.json_normalize(
    data, 
    record_path =['students'], 
    meta=['school_name', 'class']
)
print('\nThe final flattened dataframe flat_df with all colums - id, name, math, physics, chemistry, school_name, class:')
print(flat_df)
print(type(flat_df))
