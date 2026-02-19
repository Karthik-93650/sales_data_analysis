import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("sales_data.xlsx")

print(df.head())
print(df.info())
print(df.describe())
total_sales = df["Sales"].sum()

print("Total Sales:", total_sales)
sales_by_product = df.groupby("Product")["Sales"].sum()
print(sales_by_product)

sales_by_region = df.groupby("Region")["Sales"].sum()
print(sales_by_region)

sales_by_product.plot(kind="bar", title="Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

sales_by_region.plot(kind="pie", autopct="%1.1f%%", title="Sales by Region")
plt.ylabel("")
plt.show()

sales_by_product.to_csv("sales_by_product.csv")
sales_by_region.to_csv("sales_by_region.csv")
