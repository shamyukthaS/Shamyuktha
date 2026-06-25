import pandas as pd
import numpy as np
products = pd.read_csv("products.csv")
sales = pd.read_csv("sales.csv")
print(products.head())
print(sales.head())
print(products.isnull().sum())
print(sales.isnull().sum())
products.fillna(0, inplace=True)
sales.fillna(0, inplace=True)
merged = pd.merge(
    sales,
    products,
    on="product_id"
)
print(merged.head())
merged["revenue"] = (
    merged["quantity"] *
    merged["price"]
)
print(merged.head())
merged["cost_amount"] = (
    merged["quantity"] *
    merged["cost"]
)
merged["profit"] = (
    merged["revenue"] -
    merged["cost_amount"]
)
merged["profit_margin"] = np.round(
(
merged["profit"] /
merged["revenue"]
) * 100,
2
)
print(merged.head())
merged["discount_percentage"] = 10
print(merged.head())
product_summary = merged.groupby(
    "product_name"
)["revenue"].sum()
print(product_summary)
store_summary = merged.groupby(
    "store_id"
)["revenue"].sum()
print(store_summary)
top_products = merged.groupby(
    "product_name"
)["quantity"].sum()
top_products = top_products.sort_values(
    ascending=False
)
print(top_products.head())
bottom_products = merged.groupby(
    "product_name"
)["quantity"].sum()
bottom_products = bottom_products.sort_values()
print(bottom_products.head())
report = merged.groupby(
    "product_name"
)[
    ["revenue",
     "profit",
     "profit_margin"]
].mean()
print(report)
merged.to_csv(
    "cleaned_sales_data.csv",
    index=False
)
report.to_csv(
    "sales_report.csv"
)
print("files exported successfully")