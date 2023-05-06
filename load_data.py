import pandas as pd

data = pd.read_csv("./data/financial-report.csv")
# pd.read_excel() -> for excel files and many more methods!

print(data.head())
print(data.tail())
