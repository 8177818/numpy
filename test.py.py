import pandas as pd
import numpy as np

df = pd.read_csv("Grocery_Inventory_and_Sales_Dataset.csv")

df.columns = df.columns.str.strip()

print(df.columns)
print(df.head())

possible_cols = ["Product Name", "ProductName", "product name", "Item", "Product"]

product_col = next((c for c in possible_cols if c in df.columns), None)

if product_col is None:
    print("No product column found")
else:
    product = df[product_col].values
    print(product[:10])