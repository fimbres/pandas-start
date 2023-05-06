import re
import pandas as pd

data = pd.read_csv("./data/financial-report.csv")

# filtering data

print(data.loc[data['Period'] > 2018]) # fitlering based in a condition

print(data.loc[(data['Period'] > 2017) & (data['Period'] < 2020)]) # complex filtering with and operand

print(data.loc[(data['Period'] > 2016) | (data['Period'] < 2018)]) # complex filtering with or operand

print(data.loc[data['Series_reference'].str.contains('AA')]) # filtering based on a value

print(data.loc[data['Series_reference'].str.contains('^BDCQ.SF[1-5]*', flags=re.I, regex=True)]) # filtering using regex
