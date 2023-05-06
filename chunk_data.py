import pandas as pd

# making chunks of data
pdd = pd.read_csv("./data/financial-report.csv")
new_data = pd.DataFrame(columns=pdd.columns)

for data in pd.read_csv("./data/financial-report.csv", chunksize=5):
    print("chunk: ", data) # printing chunks
    results = data.groupby(['Period']).count()
    new_data = pd.concat([new_data, results])


new_data.to_csv("./data/chunk-report.csv")
