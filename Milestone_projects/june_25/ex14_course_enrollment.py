from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def create_enrollment_file():
    with open("/tmp/enrollments.txt", "w") as f:
        f.write("Python,Rahul\nPython,Priya\nSQL,Amit\nPython,Sneha\nPower BI,Kiran\nSQL,Megha\nPower BI,Arjun")


def count_students():
    courses = {}
    with open("/tmp/enrollments.txt", "r") as f:
        for line in f:
            course, _ = line.strip().split(",")
            courses[course] = courses.get(course, 0) + 1
    with open("/tmp/enrollment_result.txt", "w") as f:
        for c, count in courses.items():
            f.write(f"{c},{count}\n")
    print(courses)


def generate_course_report():
    with open("/tmp/enrollment_result.txt", "r") as f:
        lines = f.readlines()
    with open("/tmp/course_report.txt", "w") as f:
        f.write("=== Course Enrollment Report ===\n")
        for line in lines:
            c, count = line.strip().split(",")
            f.write(f"{c} = {count}\n")
    print("course_report.txt generated")


with DAG(
    dag_id="ex14_course_enrollment",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["capstone"]
) as dag:

    t1 = PythonOperator(task_id="create_enrollment_file", python_callable=create_enrollment_file)
    t2 = PythonOperator(task_id="count_students", python_callable=count_students)
    t3 = PythonOperator(task_id="generate_course_report", python_callable=generate_course_report)

    t1 >> t2 >> t3
