from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def create_result_file():
    with open("/tmp/results.txt", "w") as f:
        f.write("Rahul,Pass\nPriya,Fail\nAmit,Pass\nSneha,Pass\nKiran,Fail\nMegha,Pass")


def count_pass_fail():
    p = f = 0
    with open("/tmp/results.txt", "r") as fi:
        for line in fi:
            _, r = line.strip().split(",")
            if r == "Pass":
                p += 1
            else:
                f += 1
    with open("/tmp/result_calc.txt", "w") as fi:
        fi.write(f"{p},{f}\n")
    print(f"Pass={p}, Fail={f}")


def generate_result_summary():
    with open("/tmp/result_calc.txt", "r") as f:
        p, fa = f.read().strip().split(",")
    with open("/tmp/result_summary.txt", "w") as f:
        f.write("=== Exam Result Summary ===\n")
        f.write(f"Total Pass = {p}\n")
        f.write(f"Total Fail = {fa}\n")
    print("result_summary.txt generated")


with DAG(
    dag_id="ex9_exam_result",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["capstone"]
) as dag:

    t1 = PythonOperator(task_id="create_result_file", python_callable=create_result_file)
    t2 = PythonOperator(task_id="count_pass_fail", python_callable=count_pass_fail)
    t3 = PythonOperator(task_id="generate_result_summary", python_callable=generate_result_summary)

    t1 >> t2 >> t3
