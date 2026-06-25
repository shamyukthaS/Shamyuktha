from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def create_transactions():
    with open("/tmp/transactions.txt", "w") as f:
        f.write("Deposit,10000\nWithdraw,2500\nDeposit,4000\nWithdraw,1500\nDeposit,2000")


def calculate_balance():
    deposit = withdraw = 0
    with open("/tmp/transactions.txt", "r") as f:
        for line in f:
            t, amt = line.strip().split(",")
            if t == "Deposit":
                deposit += int(amt)
            else:
                withdraw += int(amt)
    balance = deposit - withdraw
    with open("/tmp/balance_result.txt", "w") as f:
        f.write(f"{deposit},{withdraw},{balance}\n")
    print(f"Deposit={deposit}, Withdraw={withdraw}, Balance={balance}")


def generate_account_report():
    with open("/tmp/balance_result.txt", "r") as f:
        deposit, withdraw, balance = f.read().strip().split(",")
    with open("/tmp/account_report.txt", "w") as f:
        f.write("=== Bank Account Report ===\n")
        f.write(f"Total Deposit = {deposit}\n")
        f.write(f"Total Withdrawal = {withdraw}\n")
        f.write(f"Final Balance = {balance}\n")
    print("account_report.txt generated")


with DAG(
    dag_id="ex12_bank_transactions",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["capstone"]
) as dag:

    t1 = PythonOperator(task_id="create_transactions", python_callable=create_transactions)
    t2 = PythonOperator(task_id="calculate_balance", python_callable=calculate_balance)
    t3 = PythonOperator(task_id="generate_account_report", python_callable=generate_account_report)

    t1 >> t2 >> t3
