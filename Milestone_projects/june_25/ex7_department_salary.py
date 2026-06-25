from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def create_department_file():
    with open("/tmp/departments.txt", "w") as f:
        f.write("IT,45000\nHR,35000\nFinance,50000\nIT,55000\nFinance,40000\nHR,30000")


def calculate_department_salary():
    dept = {}
    with open("/tmp/departments.txt", "r") as f:
        for line in f:
            d, s = line.strip().split(",")
            dept[d] = dept.get(d, 0) + int(s)
    with open("/tmp/dept_result.txt", "w") as f:
        for d, s in dept.items():
            f.write(f"{d},{s}\n")
    print(dept)


def generate_department_report():
    with open("/tmp/dept_result.txt", "r") as f:
        lines = f.readlines()
    with open("/tmp/department_report.txt", "w") as f:
        f.write("=== Department Salary Report ===\n")
        for line in lines:
            d, s = line.strip().split(",")
            f.write(f"{d} = {s}\n")
    print("department_report.txt generated")


with DAG(
    dag_id="ex7_department_salary",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["capstone"]
) as dag:

    t1 = PythonOperator(task_id="create_department_file", python_callable=create_department_file)
    t2 = PythonOperator(task_id="calculate_department_salary", python_callable=calculate_department_salary)
    t3 = PythonOperator(task_id="generate_department_report", python_callable=generate_department_report)

    t1 >> t2 >> t3
