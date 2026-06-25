from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def create_employee_file():
    with open("/tmp/employees.txt", "w") as f:
        f.write("Rahul,28\nPriya,31\nAmit,42\nSneha,26\nKiran,38")


def calculate_average_age():
    data = {}
    with open("/tmp/employees.txt", "r") as f:
        for line in f:
            name, age = line.strip().split(",")
            data[name] = int(age)
    youngest = min(data, key=data.get)
    oldest = max(data, key=data.get)
    avg = sum(data.values()) / len(data)
    with open("/tmp/age_result.txt", "w") as f:
        f.write(f"{youngest},{data[youngest]},{oldest},{data[oldest]},{avg:.1f}\n")
    print(f"Youngest={youngest}, Oldest={oldest}, Avg={avg:.1f}")


def generate_age_report():
    with open("/tmp/age_result.txt", "r") as f:
        youngest, y_age, oldest, o_age, avg = f.read().strip().split(",")
    with open("/tmp/age_report.txt", "w") as f:
        f.write("=== Employee Age Report ===\n")
        f.write(f"Youngest Employee = {youngest} ({y_age} yrs)\n")
        f.write(f"Oldest Employee = {oldest} ({o_age} yrs)\n")
        f.write(f"Average Age = {avg} yrs\n")
    print("age_report.txt generated")


with DAG(
    dag_id="ex13_employee_age",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["capstone"]
) as dag:

    t1 = PythonOperator(task_id="create_employee_file", python_callable=create_employee_file)
    t2 = PythonOperator(task_id="calculate_average_age", python_callable=calculate_average_age)
    t3 = PythonOperator(task_id="generate_age_report", python_callable=generate_age_report)

    t1 >> t2 >> t3
