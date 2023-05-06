import pandas as pd

data = pd.read_csv("./data/financial-report.csv")

# writing data

print(data.head())

data = data.drop(columns=['Series_reference']) # deleting columns

print(data.head())

data['New column'] = data['Period'] * 25 # adding a new column

print(data.head()) # printing the new file

data.to_csv('./data/updated-report.csv') # saving the changes
