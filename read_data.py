import pandas as pd

data = pd.read_csv("./data/financial-report.csv")

# reading data

print(data.columns) # read headers of each column

print(data[['Series_reference', 'Period']]) #all data for the selected colums

print(data.iloc[2, 1]) # read a specific cell

print(data.iloc[0: 4]) # you can also read entire rows

print(data.loc[data['Period'] > 2017]) # read data based on a certain condition

print(data.sort_values('Period', ascending=True)) # sort data based in values of a column

print(data.describe()) # calculate properties of the values of each column

for index, row in data.iterrows(): # iterating each row
    print(index, row['Series_reference'])
