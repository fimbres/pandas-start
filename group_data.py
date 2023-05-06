import pandas as pd

data = pd.read_csv("./data/financial-report.csv")

# grouping data

data['count'] = 1

print(data.groupby(['Period']).count()['count'])
