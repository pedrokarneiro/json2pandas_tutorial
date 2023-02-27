###################################################################################################
# Pandas convert JSON into a DataFrame
# 2. Reading simple JSON from a URL
# Source: https://towardsdatascience.com/how-to-convert-json-into-a-pandas-dataframe-100b2ae1e0d8
###################################################################################################
import pandas as pd

URL = 'http://raw.githubusercontent.com/BindiChen/machine-learning/master/data-analysis/027-pandas-convert-json/data/simple.json'
df = pd.read_json(URL)
print(df)
print(df.info())
