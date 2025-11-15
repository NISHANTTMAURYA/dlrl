import pandas as pd

df = pd.read_csv('test_measure.csv')

# Print column names
print("Column names:")
print(df.columns.tolist())

# Display first few rows
print("\nFirst 5 rows:")
print(df.head())