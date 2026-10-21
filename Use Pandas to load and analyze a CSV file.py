import pandas as pd

df = pd.read_csv("data.csv")
print("First 5 rows:\n", df.head())
print("Summary statistics:\n", df.describe())
print("Column names:", df.columns)
