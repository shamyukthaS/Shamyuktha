# Week 4 - Azure Databricks

## Project

Employee Attendance Tracker

---

## Objective

The objective of Week 4 is to build an end-to-end ETL pipeline using Azure Databricks following the Medallion Architecture (Bronze, Silver, Gold).

---

## Technologies Used

- Azure Databricks
- Delta Lake
- Apache Spark
- SQL
- Python

---

## Input Files

- employee.csv
- attendance.csv
- tasks.csv

---

## Bronze Layer

- bronze_employee
- bronze_attendance
- bronze_tasks

---

## Silver Layer

Created cleaned and transformed employee dataset by:

- Removing duplicate records
- Joining employee, attendance, and task datasets
- Calculating work hours
- Calculating effective work hours
- Calculating productivity score

---

## Gold Layer

Generated business reports:

- Employee Productivity Report
- Department Summary
- Frequent Absentees Report
- Task Summary

---

## Folder Contents

- Employee_Week4.ipynb
- employee.csv
- attendance.csv
- tasks.csv
- bronze_employee.csv
- bronze_attendance.csv
- bronze_tasks.csv
- silver_employee.csv
- gold_employee_productivity.csv
- gold_department_summary.csv
- gold_absentees.csv
- gold_task_summary.csv

---

## Deliverables

- Delta Tables
- Bronze Layer
- Silver Layer
- Gold Layer
- SQL Verification
- Analytical Reports

---

## Learning Outcomes

- Azure Databricks
- Medallion Architecture
- Delta Lake
- ETL Pipeline
- Data Transformation
- Business Reporting

---

## Status

Week 4 Completed Successfully
