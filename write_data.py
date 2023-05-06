import pandas as pd

data = pd.read_csv("./data/financial-report.csv")

# writing data

data['New column'] = data['Period'] * 25 # adding a new column

print(data.head()) # printing the new file

data = data.drop(columns=['New column']) # deleting columns

print(data.head())

data.to_csv('./data/updated-report.csv') # saving the changes
