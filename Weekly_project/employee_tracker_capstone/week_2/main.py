import pandas as pd
import numpy as np
attendance = pd.read_csv("attendance.csv")
tasks = pd.read_csv("tasks.csv")
print(attendance.isnull().sum())
print(tasks.isnull().sum())
attendance.fillna("unknown", inplace=True)
tasks.fillna(0, inplace=True)
attendance["clock_in"] = pd.to_datetime(attendance["clock_in"])
attendance["clock_out"] = pd.to_datetime(attendance["clock_out"])
attendance["work_hours"] = (
attendance["clock_out"] -
attendance["clock_in"]
).dt.total_seconds()/3600
print(attendance.head())
attendance["effective_work_hours"] = attendance["work_hours"] - 1
print(attendance.head())
merged = pd.merge(
attendance,
tasks,
on="employee_id"
)
print(merged.head())
merged["productivity_score"] = np.round(
merged["tasks_completed"] /
merged["effective_work_hours"],2
)
attendance["effective_work_hours"] = attendance["work_hours"] - 1
merged["productivity_score"]
top = merged.sort_values(
by="productivity_score",
ascending=False
)
absent = merged[
merged["effective_work_hours"] < 7
]
attendance.to_csv(
"cleaned_attendance.csv",
index=False
)
tasks.to_csv(
"cleaned_tasks.csv",
index=False
)
bottom = merged.sort_values(
by="productivity_score"
)
print("\nBottom Performers")
print(bottom[[
"employee_id",
"productivity_score"
]].head())
report = merged.groupby("employee_id")[
["effective_work_hours",
"productivity_score"]
].mean()
print(report)

