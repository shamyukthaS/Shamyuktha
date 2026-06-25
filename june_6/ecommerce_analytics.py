import csv
import numpy as np
import pandas as pd
from collections import Counter

FILE = "orders.csv"

def load_orders():
    with open(FILE, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)

def get_revenue(order):
    return int(order["quantity"]) * int(order["price"])

print("1. Read orders.csv")
with open(FILE, "r") as f:
    content = f.read()
print(content)

print("2. Display all records")
orders = load_orders()
for o in orders:
    print(o)
print()

print("3. Count total orders")
print(f"Total Orders = {len(orders)}")
print()

print("4. Calculate total revenue")
total_revenue = sum(get_revenue(o) for o in orders)
print(f"Total Revenue = {total_revenue}")
print()

print("5. Highest order value")
highest = max(orders, key=get_revenue)
print(f"Highest Order Value = {get_revenue(highest)} ({highest['customer_name']})")
print()

print("6.Lowest order value")
lowest = min(orders, key=get_revenue)
print(f"Lowest Order Value = {get_revenue(lowest)} ({lowest['customer_name']})")
print()

print("7.Average order value")
avg = total_revenue / len(orders)
print(f"Average Order Value = {avg:.2f}")
print()

print("8.Display all unique customers")
unique_customers = sorted(set(o["customer_name"] for o in orders))
for c in unique_customers:
    print(c)
print()

print("9.Count unique customers")
print(f"Unique Customers = {len(unique_customers)}")
print()

print("10.Customer with highest purchase amount")
customer_totals = {}
for o in orders:
    name = o["customer_name"]
    customer_totals[name] = customer_totals.get(name, 0) + get_revenue(o)
top_customer = max(customer_totals, key=customer_totals.get)
print(f"{top_customer} = {customer_totals[top_customer]}")
print()

print("11.Count orders by product")
product_orders = Counter(o["product"] for o in orders)
for product, count in product_orders.items():
    print(f"{product} = {count}")
print()

print("12.Revenue by product")
product_revenue = {}
for o in orders:
    p = o["product"]
    product_revenue[p] = product_revenue.get(p, 0) + get_revenue(o)
for product, rev in product_revenue.items():
    print(f"{product} = {rev}")
print()

print("13.Most sold product")
product_qty = {}
for o in orders:
    p = o["product"]
    product_qty[p] = product_qty.get(p, 0) + int(o["quantity"])
most_sold = max(product_qty, key=product_qty.get)
print(f"Most Sold Product = {most_sold} (qty: {product_qty[most_sold]})")
print()

print("14.Least sold product")
least_sold = min(product_qty, key=product_qty.get)
print(f"Least Sold Product = {least_sold} (qty: {product_qty[least_sold]})")
print()

print("15.Revenue by category")
category_revenue = {}
for o in orders:
    c = o["category"]
    category_revenue[c] = category_revenue.get(c, 0) + get_revenue(o)
for category, rev in category_revenue.items():
    print(f"{category} = {rev}")
print()


print("16.Count orders by city")
city_orders = Counter(o["city"] for o in orders)
for city, count in city_orders.items():
    print(f"{city} = {count}")
print()

print("17.Revenue by city")
city_revenue = {}
for o in orders:
    c = o["city"]
    city_revenue[c] = city_revenue.get(c, 0) + get_revenue(o)
for city, rev in city_revenue.items():
    print(f"{city} = {rev}")
print()

print("18. City generating highest revenue")
top_city = max(city_revenue, key=city_revenue.get)
print(f"Top City = {top_city} (revenue: {city_revenue[top_city]})")
print()

print("19.Product names list sorted alphabetically")
products_list = sorted([o["product"] for o in orders])
print(products_list)
print()

print("20.Unique cities set")
cities_set = set(o["city"] for o in orders)
print(cities_set)
print()

print("21.Dictionary city : revenue")
city_rev_dict = {}
for o in orders:
    c = o["city"]
    city_rev_dict[c] = city_rev_dict.get(c, 0) + get_revenue(o)
print(city_rev_dict)
print()

print("22.Dictionary product : quantity_sold")
product_qty_dict = {}
for o in orders:
    p = o["product"]
    product_qty_dict[p] = product_qty_dict.get(p, 0) + int(o["quantity"])
print(product_qty_dict)
print()

def calculate_total_revenue():
    orders = load_orders()
    return sum(get_revenue(o) for o in orders)


print("23.calculate_total_revenue()")
orders = load_orders()
total_rev = sum(get_revenue(o) for o in orders)
print(f"Total Revenue = {total_rev}")
print()

print("24.find_top_product()")
orders = load_orders()
product_qty = {}
for o in orders:
    p = o["product"]
    product_qty[p] = product_qty.get(p, 0) + int(o["quantity"])
top_product = max(product_qty, key=product_qty.get)
print(f"Top Product = {top_product}")
print()

print("25.find_top_city()")
orders = load_orders()
city_revenue = {}
for o in orders:
    c = o["city"]
    city_revenue[c] = city_revenue.get(c, 0) + get_revenue(o)
top_city = max(city_revenue, key=city_revenue.get)
print(f"Top City = {top_city}")
print()

print("26. find_average_order_value()")
orders = load_orders()
total = sum(get_revenue(o) for o in orders)
avg_order = total / len(orders)
print(f"Average Order Value = {avg_order:.2f}")
print()

print("27.Handle missing CSV file")
try:
    with open("missing_file.csv", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("Error: CSV file not found.")
print()

print("28.Handle invalid quantity values")
test_rows = [
    {"order_id": "9999", "customer_name": "Test", "city": "X", "product": "Y", "category": "Z", "quantity": "abc", "price": "100"},
]
for row in test_rows:
    try:
        qty = int(row["quantity"])
    except ValueError:
        print(f"Error: Invalid quantity '{row['quantity']}' in order {row['order_id']}.")
print()

print("29.Handle invalid price values")
test_rows2 = [
    {"order_id": "9998", "customer_name": "Test", "city": "X", "product": "Y", "category": "Z", "quantity": "1", "price": "xyz"},
]
for row in test_rows2:
    try:
        price = int(row["price"])
    except ValueError:
        print(f"Error: Invalid price '{row['price']}' in order {row['order_id']}.")
print()


print("30.NumPy array of order values")
order_values = np.array([get_revenue(o) for o in orders])
print(f"Order Values Array = {order_values}")
print(f"Total Revenue      = {np.sum(order_values)}")
print(f"Average Revenue    = {np.mean(order_values):.2f}")
print(f"Maximum Revenue    = {np.max(order_values)}")
print(f"Minimum Revenue    = {np.min(order_values)}")
print(f"Standard Deviation = {np.std(order_values):.2f}")
print()


print("31.Read CSV using Pandas")
df = pd.read_csv(FILE)
print(df)
print()

print("32.Create Revenue Column")
df["revenue"] = df["quantity"] * df["price"]
print(df[["order_id", "customer_name", "product", "quantity", "price", "revenue"]])
print()

print("33.Top 5 highest value orders")
top5 = df.nlargest(5, "revenue")
print(top5[["order_id", "customer_name", "product", "revenue"]])
print()

print("34.Group by city and calculate revenue")
city_group = df.groupby("city")["revenue"].sum().reset_index()
print(city_group)
print()

print("35.Group by product and calculate revenue")
product_group = df.groupby("product")["revenue"].sum().reset_index()
print(product_group)
print()

print("36.Top selling products")
top_selling = df.groupby("product")["quantity"].sum().sort_values(ascending=False).reset_index()
print(top_selling)
print()

print("37.City-wise order count")
city_count = df.groupby("city")["order_id"].count().reset_index()
city_count.columns = ["city", "order_count"]
print(city_count)
print()


print("REPORT GENERATION")
print()

orders = load_orders()
order_vals = [get_revenue(o) for o in orders]
cat_rev = {}
for o in orders:
    c = o["category"]
    cat_rev[c] = cat_rev.get(c, 0) + get_revenue(o)
city_rev = {}
for o in orders:
    c = o["city"]
    city_rev[c] = city_rev.get(c, 0) + get_revenue(o)

report = f"""===== Report =====

Total Orders         : {len(orders)}
Total Revenue        : {sum(order_vals)}
Average Order Value  : {sum(order_vals)/len(order_vals):.2f}
Highest Order Value  : {max(order_vals)}
Lowest Order Value   : {min(order_vals)}

Revenue By City:
"""
for city, rev in sorted(city_rev.items()):
    report += f"  {city:<15} : {rev}\n"

report += "\nRevenue By Category:\n"
for cat, rev in sorted(cat_rev.items()):
    report += f"  {cat:<15} : {rev}\n"

pq = {}
for o in orders:
    pq[o["product"]] = pq.get(o["product"], 0) + int(o["quantity"])
top_prod = max(pq, key=pq.get)
top_rev_city = max(city_rev, key=city_rev.get)

report += f"\nTop Selling Product      : {top_prod}\n"
report += f"Top Revenue Generating City : {top_rev_city}\n"

with open("sales_summary_report.txt", "w") as f:
    f.write(report)

print("File 'sales_summary_report.txt' created.")
print(report)


print("BONUS TASKS")
print()

print("38.high_value_orders.csv (orders above 50000)")
high_value = df[df["revenue"] > 50000]
high_value.to_csv("high_value_orders.csv", index=False)
print("File 'high_value_orders.csv' created.")
print(high_value.to_string(index=False))
print()

print("39.electronics_orders.csv (Electronics only)")
electronics = df[df["category"] == "Electronics"]
electronics.to_csv("electronics_orders.csv", index=False)
print("File 'electronics_orders.csv' created.")
print(electronics.to_string(index=False))
print()

print("40.Menu-Driven Application")

def view_orders():
    orders = load_orders()
    print(f"\n{'ID':<8}{'Customer':<16}{'City':<12}{'Product':<10}{'Category':<16}{'Qty':<6}{'Price':<10}{'Revenue'}")
    for o in orders:
        rev = get_revenue(o)
        print(f"{o['order_id']:<8}{o['customer_name']:<16}{o['city']:<12}{o['product']:<10}{o['category']:<16}{o['quantity']:<6}{o['price']:<10}{rev}")

def revenue_analysis():
    orders = load_orders()
    vals = [get_revenue(o) for o in orders]
    print(f"\nTotal Revenue        : {sum(vals)}")
    print(f"Highest Order Value  : {max(vals)}")
    print(f"Lowest Order Value   : {min(vals)}")
    print(f"Average Order Value  : {sum(vals)/len(vals):.2f}")

def product_analysis():
    orders = load_orders()
    pq = {}
    pr = {}
    for o in orders:
        p = o["product"]
        pq[p] = pq.get(p, 0) + int(o["quantity"])
        pr[p] = pr.get(p, 0) + get_revenue(o)
    print(f"\n{'Product':<12}{'Qty Sold':<12}{'Revenue'}")
    for p in sorted(pq):
        print(f"{p:<12}{pq[p]:<12}{pr[p]}")
    print(f"\nMost Sold  : {max(pq, key=pq.get)}")
    print(f"Least Sold : {min(pq, key=pq.get)}")

def city_analysis():
    orders = load_orders()
    cr = {}
    cc = Counter(o["city"] for o in orders)
    for o in orders:
        c = o["city"]
        cr[c] = cr.get(c, 0) + get_revenue(o)
    print(f"\n{'City':<14}{'Orders':<10}{'Revenue'}")
    for city in sorted(cr):
        print(f"{city:<14}{cc[city]:<10}{cr[city]}")
    print(f"\nTop Revenue City : {max(cr, key=cr.get)}")

def export_reports():
    df = pd.read_csv(FILE)
    df["revenue"] = df["quantity"] * df["price"]
    df[df["revenue"] > 50000].to_csv("high_value_orders.csv", index=False)
    df[df["category"] == "Electronics"].to_csv("electronics_orders.csv", index=False)
    print("\nExported: high_value_orders.csv")
    print("Exported: electronics_orders.csv")

menu_options = {
    "1": ("View Orders", view_orders),
    "2": ("Revenue Analysis", revenue_analysis),
    "3": ("Product Analysis", product_analysis),
    "4": ("City Analysis", city_analysis),
    "5": ("Export Reports", export_reports),
}

print("\nRunning all menu options automatically:")
for key in ["1", "2", "3", "4", "5"]:
    label, func = menu_options[key]
    print(f"\n[{key}] {label}")
    func()

print("\n[6] Exit")
print("Exiting application.")
