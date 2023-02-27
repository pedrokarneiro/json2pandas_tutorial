###################################################################################################
# Pandas convert JSON into a DataFrame
# 1. Reading simple JSON from a local file
# Source: https://towardsdatascience.com/how-to-convert-json-into-a-pandas-dataframe-100b2ae1e0d8
###################################################################################################
import pandas as pd

df = pd.read_json('simple.json')
print(df)
print(df.info())
