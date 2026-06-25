create database hospital_capstone_db;
use hospital_capstone_db;
-- patients 
create table patients
(
    patient_id int primary key,
    patient_name varchar(100),
    gender varchar(10),
    age int,
    city varchar(50),
    phone varchar(15)
);
-- department
create table departments
(
    department_id int primary key,
    department_name varchar(100)
);
-- doctors
create table doctors
(
    doctor_id int primary key,
    doctor_name varchar(100),
    specialization varchar(100),
    department_id int,
    consultation_fee decimal(10,2),
    foreign key (department_id)
    references departments(department_id)
);
-- appointments
create table appointments
(
    appointment_id int primary key,
    patient_id int,
    doctor_id int,
    appointment_date date,
    appointment_status varchar(30),
    foreign key (patient_id)
    references patients(patient_id),
    foreign key (doctor_id)
    references doctors(doctor_id)
);
-- treatments
create table treatments
(
    treatment_id int primary key,
    appointment_id int,
    treatment_name varchar(100),
    treatment_cost decimal(10,2),
    foreign key (appointment_id)
    references appointments(appointment_id)
);
-- bills
create table bills
(
    bill_id int primary key,
    patient_id int,
    appointment_id int,
    bill_date date,
    total_amount decimal(10,2),
    bill_status varchar(30),
    foreign key (patient_id)
    references patients(patient_id),
    foreign key (appointment_id)
    references appointments(appointment_id)
);
-- payments
create table payments
(
    payment_id int primary key,
    bill_id int,
    payment_mode varchar(30),
    paid_amount decimal(10,2),
    payment_status varchar(30),
    foreign key (bill_id)
    references bills(bill_id)
);
-- insert into departments
insert into departments values
(1,'cardiology'),
(2,'neurology'),
(3,'orthopedics'),
(4,'pediatrics'),
(5,'general medicine');
-- insert into doctors
insert into doctors values
(101,'dr. arun', 'cardiology',1,1000.00),
(102,'dr. priya', 'neurology',2,1200.00),
(103,'dr. karthik', 'orthopedics',3,900.00),
(104,'dr. divya', 'pediatrics',4,700.00),
(105,'dr. vignesh', 'general medicine',5,600.00),
(106,'dr. nandhini', 'cardiology',1,1100.00),
(107,'dr. surya', 'orthopedics',3,950.00),
(108,'dr. harini', 'neurology',2,1300.00);
-- insert into patients
insert into patients values
(1,'arun kumar','male',35,'chennai','9876543210'),
(2,'priya','female',42,'hyderabad','9876543211'),
(3,'karthik','male',28,'coimbatore','9876543212'),
(4,'divya','female',50,'hyderabad','9876543213'),
(5,'vignesh','male',39,'chennai','9876543214'),
(6,'keerthana','female',31,'salem','9876543215'),
(7,'suresh','male',45,'madurai','9876543216'),
(8,'nandhini','female',37,'chennai','9876543217'),
(9,'prakash','male',55,'erode','9876543218'),
(10,'harini','female',29,'coimbatore','9876543219'),
(11,'mohan','male',41,'vellore','9876543220'),
(12,'kavya','female',33,'chennai','9876543221');
-- insert intp appointments
insert into appointments values
(1001,1,101,'2026-01-05','completed'),
(1002,2,102,'2026-01-06','completed'),
(1003,3,103,'2026-01-08','pending'),
(1004,4,104,'2026-01-10','cancelled'),
(1005,5,105,'2026-01-12','completed'),
(1006,6,106,'2026-01-15','completed'),
(1007,7,107,'2026-01-18','pending'),
(1008,8,108,'2026-01-20','completed'),
(1009,9,101,'2026-01-22','completed'),
(1010,10,102,'2026-01-24','cancelled'),
(1011,11,103,'2026-01-26','completed'),
(1012,12,104,'2026-01-28','pending'),
(1013,1,105,'2026-02-01','completed'),
(1014,2,106,'2026-02-03','completed'),
(1015,3,107,'2026-02-05','completed'),
(1016,4,108,'2026-02-07','pending'),
(1017,5,101,'2026-02-09','completed'),
(1018,6,102,'2026-02-11','completed'),
(1019,7,103,'2026-02-13','completed'),
(1020,8,104,'2026-02-15','pending');
-- insert into treatments
insert into treatments values
(1,1001,'ecg',1500.00),
(2,1002,'brain scan',4500.00),
(3,1003,'fracture treatment',3500.00),
(4,1005,'general checkup',800.00),
(5,1006,'heart screening',3000.00),
(6,1008,'neurology consultation',2500.00),
(7,1009,'ecg',1500.00),
(8,1011,'bone scan',2800.00),
(9,1013,'general checkup',800.00),
(10,1014,'heart screening',3000.00),
(11,1015,'fracture treatment',3500.00),
(12,1017,'ecg',1500.00),
(13,1018,'brain scan',4500.00),
(14,1019,'bone scan',2800.00),
(15,1020,'vaccination',1000.00);
-- insert into bills
insert into bills values
(1,1,1001,'2026-01-05',2500.00,'paid'),
(2,2,1002,'2026-01-06',6000.00,'paid'),
(3,3,1003,'2026-01-08',5000.00,'unpaid'),
(4,5,1005,'2026-01-12',1800.00,'paid'),
(5,6,1006,'2026-01-15',4500.00,'paid'),
(6,8,1008,'2026-01-20',3800.00,'paid'),
(7,9,1009,'2026-01-22',2500.00,'paid'),
(8,11,1011,'2026-01-26',4200.00,'paid'),
(9,1,1013,'2026-02-01',1800.00,'paid'),
(10,2,1014,'2026-02-03',4500.00,'paid'),
(11,3,1015,'2026-02-05',5000.00,'paid'),
(12,5,1017,'2026-02-09',2500.00,'paid'),
(13,6,1018,'2026-02-11',6000.00,'paid'),
(14,7,1019,'2026-02-13',4200.00,'paid'),
(15,8,1020,'2026-02-15',2000.00,'unpaid');
-- insert into payments
insert into payments values
(1,1,'upi',2500.00,'success'),
(2,2,'card',6000.00,'success'),
(3,3,'upi',0.00,'pending'),
(4,4,'cash',1800.00,'success'),
(5,5,'upi',4500.00,'success'),
(6,6,'card',3800.00,'success'),
(7,7,'upi',2500.00,'success'),
(8,8,'net banking',4200.00,'success'),
(9,9,'upi',1800.00,'success'),
(10,10,'card',4500.00,'success'),
(11,11,'upi',5000.00,'success'),
(12,12,'cash',2500.00,'success'),
(13,13,'upi',6000.00,'success'),
(14,14,'net banking',4200.00,'success'),
(15,15,'upi',0.00,'pending');
select * from patients;
select * from doctors;*
select *
from patients
where city = 'hyderabad';
select *
from doctors
where specialization = 'cardiology';
select *
from appointments
where appointment_date > '2026-01-01';
select *
from appointments
where appointment_status = 'cancelled;
select *
from bills
where total_amount > 5000;
select *
from payments
where payment_mode = 'upi';
select *
from patients
where age between 30 and 50;
select *
from doctors
where consultation_fee > 800;
select count(*) as total_patients
from patients;
select count(*) as total_doctors
from doctors;
select count(*) as total_appointments
from appointments;
select avg(consultation_fee) as average_fee
from doctors;
select max(treatment_cost) as highest_treatment_cost
from treatments;
select sum(total_amount) as total_billing
from bills;
select sum(paid_amount) as total_paid
from payments;
select city,count(*) as total_patients
from patients
group by city;
select specialization,
count(*) as total_doctors
from doctors
group by specialization;
select appointment_status,
count(*) as total_appointments
from appointments
group by appointment_status;
select p.patient_name,
a.appointment_date,
a.appointment_status
from patients p
join appointments a
on p.patient_id = a.patient_id;
select d.doctor_name,
dp.department_name
from doctors d
join departments dp
on d.department_id = dp.department_id;
select p.patient_name,
       d.doctor_name,
       a.appointment_date
from appointments a
join patients p
on a.patient_id = p.patient_id
join doctors d
on a.doctor_id = d.doctor_id;
select a.appointment_id,
t.treatment_name,
t.treatment_cost
from appointments a
join treatments t
on a.appointment_id = t.appointment_id;
select b.bill_id,
p.patient_name,
b.total_amount
from bills b
join patients p
on b.patient_id = p.patient_id;
select b.bill_id,
p.payment_mode,
p.paid_amount,
p.payment_status
from bills b
join payments p
on b.bill_id = p.bill_id;
select p.patient_name,
d.doctor_name,
dp.department_name,
a.appointment_date,
a.appointment_status,
t.treatment_name,
t.treatment_cost,
b.total_amount,
py.payment_status
from appointments a
join patients p
on a.patient_id = p.patient_id
join doctors d
on a.doctor_id = d.doctor_id
join departments dp
on d.department_id = dp.department_id
left join treatments t
on a.appointment_id = t.appointment_id
left join bills b
on a.appointment_id = b.appointment_id
left join payments py
on b.bill_id = py.bill_id;
select d.doctor_name,
count(a.appointment_id) as total_appointments
from doctors d
join appointments a
on d.doctor_id = a.doctor_id
group by d.doctor_name;
select dp.department_name,
count(a.appointment_id) as total_appointments
from departments dp
join doctors d
on dp.department_id = d.department_id
join appointments a
on d.doctor_id = a.doctor_id
group by dp.department_name;
select dp.department_name,
sum(b.total_amount) as total_revenue
from departments dp
join doctors d
on dp.department_id = d.department_id
join appointments a
on d.doctor_id = a.doctor_id
join bills b
on a.appointment_id = b.appointment_id
group by dp.department_name;
select dp.department_name,
sum(b.total_amount) as total_revenue
from departments dp
join doctors d
on dp.department_id = d.department_id
join appointments a
on d.doctor_id = a.doctor_id
join bills b
on a.appointment_id = b.appointment_id
group by dp.department_name
having sum(b.total_amount) > 20000;
select city,
count(*) as total_patients
from patients
group by city
having count(*) > 2;
select * from patients where patient_id in
(
select patient_id
from appointments
);
select *from patients where patient_id not in
(
    select patient_id
    from appointments
);
select *from patients where patient_id not in
(
    select patient_id
    from appointments
);
select *from doctors where doctor_id not in
(
    select doctor_id
    from appointments
);
select * from bills where total_amount >
(
    select avg(total_amount)
    from bills
);
select p.patient_name,
       b.total_amount
from patients p join bills b
on p.patient_id = b.patient_id
where b.total_amount =
(
    select max(total_amount)
    from bills
);
select * from doctors where consultation_fee >
(
    select avg(consultation_fee)
    from doctors
);
select distinct p.patient_name from patients p
join appointments a
on p.patient_id = a.patient_id
join doctors d
on a.doctor_id = d.doctor_id
where d.specialization = 'cardiology';
select * from bills where bill_status = 'unpaid';
select * from appointments
where appointment_id in
(
    select appointment_id
    from treatments
);
select p.patient_name, sum(b.total_amount) as total_bill
from patients p join bills b
on p.patient_id = b.patient_id
group by p.patient_id, p.patient_name
having sum(b.total_amount) >
( select avg(patient_total) from(select sum(total_amount) as patient_total
from bills group by patient_id) as avg_bill
);
select * from appointments where appointment_id not in
(
    select appointment_id
    from treatments
);
select * from bills where bill_id not in
(
    select bill_id
    from payments
);
select * from payments where paid_amount is null
or paid_amount = 0;
select a.* from appointments a join bills b
on a.appointment_id = b.appointment_id
where a.appointment_status = 'cancelled';
select b.bill_id,b.total_amount,p.paid_amount
from bills b join payments p
on b.bill_id = p.bill_id
where p.paid_amount < b.total_amount;
select * from doctors
where department_id not in
(select department_id from departments
);
select * from appointments where patient_id not in
(select patient_id from patients
)
or doctor_id not in
( select doctor_id from doctors);
select p.patient_name,p.city,
count(a.appointment_id) as total_appointments,
sum(b.total_amount) as total_bill_amount,
sum(py.paid_amount) as total_paid_amount,
sum(b.total_amount) - sum(py.paid_amount) as pending_amount
from patients p join appointments a
on p.patient_id = a.patient_id
join bills b
on p.patient_id = b.patient_id
join payments py
on b.bill_id = py.bill_id
group by p.patient_id,
p.patient_name,
p.city;










