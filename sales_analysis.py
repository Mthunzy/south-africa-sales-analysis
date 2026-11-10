# South Africa Sales Analysis
# By Mthunzi Ntombela

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('sales_data.csv')

# 1. Clean data - remove missing values
df = df.dropna()
print(f"Total rows after cleaning: {len(df)}")

# 2. Total sales by product
sales_by_product = df.groupby('Product')['Sales'].sum().sort_values(ascending=False)
print("\nSales by Product:")
print(sales_by_product)

# 3. Total sales by month
sales_by_month = df.groupby('Month')['Sales'].sum()
print("\nSales by Month:")
print(sales_by_month)

# 4. Top product
top_product = sales_by_product.index[0]
print(f"\nTop Selling Product: {top_product}")

# 5. Chart - Sales by Product
sales_by_product.plot(kind='bar', title='Sales by Product')
plt.ylabel('Sales (R)')
plt.show()

# 6. Chart - Sales by Month
sales_by_month.plot(kind='line', marker='o', title='Sales by Month')
plt.ylabel('Sales (R)')
plt.show()
