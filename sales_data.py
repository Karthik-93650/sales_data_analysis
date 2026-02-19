import pandas as pd
import matplotlib.pyplot as plt
import os

FILE_NAME = "sales_data.xlsx"

# STEP 1: Define new row (THIS IS NOT CMD INPUT)
new_row = {
    "Date": "2026-02-19",
    "Product": "Laptop",
    "Region": "India",
    "Sales": 50000,
    "Quantity": 1
}

# STEP 2: If file exists → read, else → create
if os.path.exists(FILE_NAME):
    df = pd.read_excel(FILE_NAME)
else:
    df = pd.DataFrame(columns=new_row.keys())

# STEP 3: Append new row
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

# STEP 4: Save back to Excel
df.to_excel(FILE_NAME, index=False)

# STEP 5: Analysis
print(df.head())
print(df.info())
print(df.describe())

total_sales = df["Sales"].sum()
print("Total Sales:", total_sales)

sales_by_product = df.groupby("Product")["Sales"].sum()
sales_by_region = df.groupby("Region")["Sales"].sum()

# STEP 6: Charts
sales_by_product.plot(kind="bar", title="Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

sales_by_region.plot(kind="pie", autopct="%1.1f%%", title="Sales by Region")
plt.ylabel("")
plt.show()
