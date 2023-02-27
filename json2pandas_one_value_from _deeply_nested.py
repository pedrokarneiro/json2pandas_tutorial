###################################################################################################
# Pandas convert JSON into a DataFrame
# 5. Extracting a value from deeply nested JSON
# Source: https://towardsdatascience.com/how-to-convert-json-into-a-pandas-dataframe-100b2ae1e0d8
###################################################################################################
import pandas as pd
import json # not used in this example.
from glom import glom

# This one gets the whole thing and the students as a long gut of nested stuff in it.
df = pd.read_json('data/nested_deep.json')
print(df)

# In other words, it gets the students as a dictionary...
print()
print('school_name is a ', type(df['school_name'][0]))
print('class is a ', type(df['class'][0]))
print('students is a ', type(df['students'][0]))

# How can we do that more effectively? The answer is using read_json with glom.
# glom is a Python library that allows us to use . notation to access property from a deeply nested object.
math = df['students'].apply(lambda row: glom(row, 'grade.math'))
print('\nmath:')
print(math)
print()
print('math is a ', type(math[0]))

# More examples:
# school_name
school_name = df['school_name']
print('\nschool_name:')
print(school_name)

# students.id
students_id = df['students'].apply(lambda row: glom(row, 'id'))
print('\nstudents_id:')
print(students_id)

# physics
math = df['students'].apply(lambda row: glom(row, 'grade.physics'))
print('\nphysics:')
print(math)
