salaries = [45000, 55000, 65000, 75000, 85000]
salaries = [45000, 55000, 65000, 75000, 85000]
print(salaries)
print("Maximum Salary:", max(salaries))
print("Minimum Salary:", min(salaries))
print("Total Payout:", sum(salaries))
print("Average Salary:", sum(salaries) / len(salaries))
salaries.append(95000)
salaries.append(105000)
print(salaries)
salaries.remove(55000)
print(salaries)
salaries.sort()
print(salaries)
salaries.sort(reverse=True)
print(salaries)
sorted_salaries = sorted(set(salaries), reverse=True)
print("Second Highest:", sorted_salaries[1])
above_70k = [s for s in salaries if s > 70000]
print(above_70k)
employee = (101, "Rahul Sharma", "Data Engineering", 75000)
print(employee)
print("Name:", employee[1])
print("Department:", employee[2])
emp_id, name, dept, salary = employee
print(emp_id, name, dept, salary)
print("Length:", len(employee))
print("First:", employee[0])
print("Last:", employee[-1])
batch_a = {"Rahul","Priya","Amit","Sneha","Farhan"}
batch_b = {"Priya","Sneha","Neha","Arjun","Farhan"}
print(batch_a & batch_b)
print(batch_a - batch_b)
print(batch_b - batch_a)
print(batch_a | batch_b)
{'Rahul','Priya','Amit','Sneha','Farhan','Neha','Arjun'}
print(batch_a ^ batch_b)
employee_info = {
    "employee_id": 101, "name": "Rahul Sharma",
    "department": "Data Engineering",
    "salary": 75000, "city": "Hyderabad"
}
print(employee_info["name"])
print("Department:", employee_info["department"])
print("City:", employee_info["city"])
employee_info["experience"] = 5
print(employee_info)
employee_info["salary"] = 85000
print("Updated Salary:", employee_info["salary"])
del employee_info["city"]
print(employee_info)
print(employee_info.keys())
print(employee_info.values())
for k, v in employee_info.items():
    print(f"{k}: {v}")
employees = [
    {"id": 101, "name": "Rahul", "department": "IT", "salary": 50000},
    {"id": 102, "name": "Priya", "department": "HR", "salary": 70000},
    {"id": 103, "name": "Amit", "department": "IT", "salary": 60000},
    {"id": 104, "name": "Sneha", "department": "Finance", "salary": 80000},
    {"id": 105, "name": "Farhan", "department": "IT", "salary": 90000}
]
for e in employees:
    print(e["name"])
it_emp = [e for e in employees if e["department"] == "IT"]
for e in it_emp:
    print(e["name"])
top = max(employees, key=lambda e: e["salary"])
print(top["name"], "-", top["salary"])
low = min(employees, key=lambda e: e["salary"])
print(low["name"], "-", low["salary"])
avg = sum(e["salary"] for e in employees) / len(employees)
print("Average:", avg)
total = sum(e["salary"] for e in employees)
print("Total:", total)
rich = [e for e in employees if e["salary"] > 70000]
for e in rich:
    print(e["name"], e["salary"])
count = sum(1 for e in employees if e["department"] == "IT")
print("IT Count:", count)
sorted_emp = sorted(employees, key=lambda e: e["salary"], reverse=True)
for e in sorted_emp:
    print(e["name"], e["salary"])
sorted_emp = sorted(employees, key=lambda e: e["salary"], reverse=True)
print(sorted_emp[1]["name"], "-", sorted_emp[1]["salary"])
depts = list(set(e["department"] for e in employees))
print(depts)
