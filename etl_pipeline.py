import pandas as pd
import sqlite3

# Extract
df = pd.read_csv('data/sales_data.csv')

# Transform
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']

# Load
conn = sqlite3.connect('sales.db')
df.to_sql('sales', conn, if_exists='replace', index=False)

print("ETL process completed and data loaded into sales.db")
