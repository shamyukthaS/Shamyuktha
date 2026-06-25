from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def create_orders():
    with open("/tmp/orders.csv", "w") as f:
        f.write("product,quantity,price\nLaptop,1,70000\nMouse,4,500\nMonitor,2,12000\nKeyboard,3,1500")


def calculate_order_value():
    revenues = {}
    with open("/tmp/orders.csv", "r") as f:
        next(f)
        for line in f:
            product, qty, price = line.strip().split(",")
            revenues[product] = int(qty) * int(price)
    with open("/tmp/order_result.txt", "w") as f:
        for p, r in revenues.items():
            f.write(f"{p},{r}\n")
    print(revenues)


def generate_sales_report():
    revenues = {}
    with open("/tmp/order_result.txt", "r") as f:
        for line in f:
            p, r = line.strip().split(",")
            revenues[p] = int(r)
    total = sum(revenues.values())
    highest = max(revenues, key=revenues.get)
    with open("/tmp/sales_report.txt", "w") as f:
        f.write("=== Sales Report ===\n")
        for p, r in revenues.items():
            f.write(f"{p} = {r}\n")
        f.write(f"\nTotal Revenue = {total}\n")
        f.write(f"Highest Selling Product = {highest}\n")
    print("sales_report.txt generated")


with DAG(
    dag_id="ex10_online_orders",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["capstone"]
) as dag:

    t1 = PythonOperator(task_id="create_orders", python_callable=create_orders)
    t2 = PythonOperator(task_id="calculate_order_value", python_callable=calculate_order_value)
    t3 = PythonOperator(task_id="generate_sales_report", python_callable=generate_sales_report)

    t1 >> t2 >> t3
