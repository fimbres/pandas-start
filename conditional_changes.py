from numpy import NaN
import pandas as pd

data = pd.read_csv("./data/financial-report.csv")

# conditional changes in data

data.loc[data['Series_title_5'] == NaN, 'Series_title_5'] = 'No value' # changing one column based on a condition

data.loc[data['Period'] > 2019, ['Series_title_4', 'Series_title_5']] = ['Test1', 'Test2'] # changin two columns at once based on a condition

print(data.tail())
