from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def create_temperature_file():
    with open("/tmp/temperature.txt", "w") as f:
        f.write("Monday,34\nTuesday,36\nWednesday,31\nThursday,38\nFriday,35\nSaturday,33\nSunday,32")


def find_highest_temperature():
    data = {}
    with open("/tmp/temperature.txt", "r") as f:
        for line in f:
            day, temp = line.strip().split(",")
            data[day] = int(temp)
    highest_day = max(data, key=data.get)
    avg = sum(data.values()) / len(data)
    with open("/tmp/temp_result.txt", "w") as f:
        f.write(f"{highest_day},{data[highest_day]},{avg:.2f}\n")
    print(f"Highest={data[highest_day]}, Avg={avg:.2f}")


def generate_weather_report():
    with open("/tmp/temp_result.txt", "r") as f:
        day, highest, avg = f.read().strip().split(",")
    with open("/tmp/weather_report.txt", "w") as f:
        f.write("=== Weather Report ===\n")
        f.write(f"Highest Temperature = {highest}C ({day})\n")
        f.write(f"Average Temperature = {avg}C\n")
    print("weather_report.txt generated")


with DAG(
    dag_id="ex11_temperature_analysis",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["capstone"]
) as dag:

    t1 = PythonOperator(task_id="create_temperature_file", python_callable=create_temperature_file)
    t2 = PythonOperator(task_id="find_highest_temperature", python_callable=find_highest_temperature)
    t3 = PythonOperator(task_id="generate_weather_report", python_callable=generate_weather_report)

    t1 >> t2 >> t3
