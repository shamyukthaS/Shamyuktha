Create database employee_tracker;
use employee_tracker;
create table employees (
    employee_id int primary key,
    employee_name varchar(100),
    department varchar(50),
    designation varchar(50),
    joining_date date
);
create table attendance (
    attendance_id int primary key,
    employee_id int,
    attendance_date date,
    clock_in datetime,
    clock_out datetime,
    foreign key (employee_id)
    references employees(employee_id)
);
create table tasks (
    task_id int primary key,
    employee_id int,
    task_name varchar(100),
    tasks_completed int,
    task_status varchar(30),
    foreign key (employee_id)
    references employees(employee_id)
);
insert into employees values
(101,'arun','it','developer','2023-01-10'),
(102,'priya','hr','executive','2022-06-15'),
(103,'karthik','finance','analyst','2021-08-20'),
(104,'sana','marketing','associate','2024-02-01'),
(105,'rahul','sales','executive','2023-07-12'),
(106,'meena','it','tester','2023-05-18'),
(107,'vikram','finance','accountant','2022-09-22'),
(108,'divya','hr','recruiter','2024-01-05'),
(109,'ajay','sales','manager','2021-11-11'),
(110,'nisha','marketing','executive','2023-03-15');
insert into attendance values
(1,101,'2026-06-01','2026-06-01 09:00:00','2026-06-01 18:00:00'),
(2,102,'2026-06-01','2026-06-01 09:20:00','2026-06-01 17:45:00'),
(3,103,'2026-06-01','2026-06-01 09:05:00','2026-06-01 18:15:00'),
(4,104,'2026-06-01','2026-06-01 10:15:00','2026-06-01 17:00:00'),
(5,105,'2026-06-01','2026-06-01 08:50:00','2026-06-01 17:30:00'),
(6,106,'2026-06-01','2026-06-01 09:10:00','2026-06-01 18:05:00'),
(7,107,'2026-06-01','2026-06-01 09:00:00','2026-06-01 18:20:00'),
(8,108,'2026-06-01','2026-06-01 09:30:00','2026-06-01 17:40:00'),
(9,109,'2026-06-01','2026-06-01 08:45:00','2026-06-01 18:10:00'),
(10,110,'2026-06-01','2026-06-01 09:50:00','2026-06-01 17:15:00'),
(11,101,'2026-06-02','2026-06-02 09:05:00','2026-06-02 18:00:00'),
(12,102,'2026-06-02','2026-06-02 09:25:00','2026-06-02 17:30:00'),
(13,103,'2026-06-02','2026-06-02 09:00:00','2026-06-02 18:10:00'),
(14,104,'2026-06-02','2026-06-02 10:30:00','2026-06-02 16:45:00'),
(15,105,'2026-06-02','2026-06-02 08:55:00','2026-06-02 17:40:00'),
(16,106,'2026-06-02','2026-06-02 09:15:00','2026-06-02 18:00:00'),
(17,107,'2026-06-02','2026-06-02 09:05:00','2026-06-02 18:15:00'),
(18,108,'2026-06-02','2026-06-02 09:40:00','2026-06-02 17:20:00'),
(19,109,'2026-06-02','2026-06-02 08:50:00','2026-06-02 18:05:00'),
(20,110,'2026-06-02','2026-06-02 10:00:00','2026-06-02 17:00:00');
insert into tasks values
(1,101,'dashboard development',8,'completed'),
(2,102,'recruitment drive',5,'completed'),
(3,103,'budget analysis',10,'completed'),
(4,104,'social media campaign',3,'pending'),
(5,105,'sales reporting',7,'completed'),
(6,106,'software testing',8,'completed'),
(7,107,'audit review',9,'completed'),
(8,108,'candidate screening',5,'completed'),
(9,109,'sales target review',10,'completed'),
(10,110,'marketing presentation',4,'pending'),
(11,101,'attendance report',7,'completed'),
(12,102,'employee onboarding',4,'completed'),
(13,103,'financial planning',9,'completed'),
(14,104,'content creation',2,'pending'),
(15,105,'inventory tracking',8,'completed'),
(16,106,'bug fixing',9,'completed'),
(17,107,'expense verification',8,'completed'),
(18,108,'training coordination',5,'completed'),
(19,109,'client meeting',10,'completed'),
(20,110,'campaign analysis',4,'pending');
select * from employees;
select * from attendance;
select * from tasks;
update attendance
set clock_out='2026-06-02 17:30:00'
where attendance_id=20;
update tasks
set task_status='completed'
where task_id=14;
delete from tasks
where task_id=20;
select *
from attendance
where time(clock_in) > '09:30:00';
select
employee_id,
attendance_date,
clock_in,
clock_out
from attendance;
select
employee_id,
attendance_date,
round(
timestampdiff(minute,clock_in,clock_out)/60,2
) as work_hours
from attendance;
select
employee_id,
round(
sum(timestampdiff(minute,clock_in,clock_out))/60,2
) as total_hours
from attendance
group by employee_id;
select
employee_id,
sum(tasks_completed) as total_tasks
from tasks
group by employee_id
order by total_tasks desc;
select
employee_id,
sum(tasks_completed) as total_tasks
from tasks
group by employee_id
having total_tasks < 10;
select
department,
count(*) as total_employees
from employees
group by department;
delimiter //
create procedure calculate_total_work_hours()
begin
select
employee_id,
round(
sum(timestampdiff(minute,clock_in,clock_out))/60,2
) as total_hours
from attendance
group by employee_id;
end //
delimiter ;
call calculate_total_work_hours();
show tables;
select count(*) from employees;
select count(*) from attendance;
select count(*) from tasks;



