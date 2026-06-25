from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def create_bill_file():
    with open("/tmp/electricity.txt", "w") as f:
        f.write("Rahul,210\nPriya,180\nAmit,300\nSneha,150\nKiran,260")


def calculate_total_units():
    units = []
    with open("/tmp/electricity.txt", "r") as f:
        for line in f:
            _, u = line.strip().split(",")
            units.append(int(u))
    total = sum(units)
    avg = total // len(units)
    with open("/tmp/bill_result.txt", "w") as f:
        f.write(f"{len(units)},{total},{avg}\n")
    print(f"Total={total}, Avg={avg}")


def generate_bill_summary():
    with open("/tmp/bill_result.txt", "r") as f:
        customers, total, avg = f.read().strip().split(",")
    with open("/tmp/bill_summary.txt", "w") as f:
        f.write("=== Electricity Bill Summary ===\n")
        f.write(f"Customers = {customers}\n")
        f.write(f"Total Units = {total}\n")
        f.write(f"Average Units = {avg}\n")
    print("bill_summary.txt generated")


with DAG(
    dag_id="ex8_electricity_bill",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["capstone"]
) as dag:

    t1 = PythonOperator(task_id="create_bill_file", python_callable=create_bill_file)
    t2 = PythonOperator(task_id="calculate_total_units", python_callable=calculate_total_units)
    t3 = PythonOperator(task_id="generate_bill_summary", python_callable=generate_bill_summary)

    t1 >> t2 >> t3
