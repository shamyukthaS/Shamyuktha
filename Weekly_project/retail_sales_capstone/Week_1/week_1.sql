create database retail_sales_dashboard;
use retail_sales_dashboard;
create table stores (
    store_id varchar(10) primary key,
    store_name varchar(100),
    region varchar(50),
    city varchar(50)
);
create table products (
    product_id varchar(10) primary key,
    product_name varchar(100),
    category varchar(50),
    price decimal(10,2),
    cost decimal(10,2)
);
create table employees (
    employee_id int primary key,
    employee_name varchar(100),
    store_id varchar(10),
    designation varchar(50),
    foreign key (store_id)
    references stores(store_id)
);
create table sales (
    sale_id int primary key,
    product_id varchar(10),
    store_id varchar(10),
    employee_id int,
    quantity int,
    sale_date date,
    foreign key (product_id)
    references products(product_id),
    foreign key (store_id)
    references stores(store_id),
    foreign key (employee_id)
    references employees(employee_id)
);
insert into stores values
('S101','Chennai Central','South','Chennai'),
('S102','Bangalore Hub','South','Bangalore'),
('S103','Mumbai Mall','West','Mumbai'),
('S104','Delhi Plaza','North','Delhi'),
('S105','Hyderabad Point','South','Hyderabad');
insert into products values
('P101','Laptop','Electronics',65000,55000),
('P102','Smartphone','Electronics',30000,25000),
('P103','Headphones','Electronics',2500,1800),
('P104','Smartwatch','Electronics',5000,3500),
('P105','Tablet','Electronics',20000,16000),
('P106','Printer','Accessories',12000,9000),
('P107','Keyboard','Accessories',1500,1000),
('P108','Mouse','Accessories',800,500),
('P109','Monitor','Electronics',15000,12000),
('P110','Webcam','Accessories',2500,1800);
insert into employees values
(201,'arun','S101','sales executive'),
(202,'priya','S102','sales executive'),
(203,'karthik','S103','sales executive'),
(204,'sana','S104','sales executive'),
(205,'rahul','S105','sales executive'),
(206,'meena','S101','sales associate'),
(207,'vikram','S102','sales associate'),
(208,'divya','S103','sales associate'),
(209,'ajay','S104','sales associate'),
(210,'nisha','S105','sales associate');
insert into sales values
(1,'P101','S101',201,2,'2026-06-01'),
(2,'P102','S102',202,3,'2026-06-01'),
(3,'P103','S103',203,5,'2026-06-01'),
(4,'P104','S104',204,4,'2026-06-01'),
(5,'P105','S105',205,2,'2026-06-01'),
(6,'P106','S101',206,3,'2026-06-01'),
(7,'P107','S102',207,8,'2026-06-01'),
(8,'P108','S103',208,10,'2026-06-01'),
(9,'P109','S104',209,2,'2026-06-01'),
(10,'P110','S105',210,4,'2026-06-01'),
(11,'P101','S101',201,1,'2026-06-02'),
(12,'P102','S102',202,2,'2026-06-02'),
(13,'P103','S103',203,6,'2026-06-02'),
(14,'P104','S104',204,3,'2026-06-02'),
(15,'P105','S105',205,1,'2026-06-02'),
(16,'P106','S101',206,2,'2026-06-02'),
(17,'P107','S102',207,7,'2026-06-02'),
(18,'P108','S103',208,9,'2026-06-02'),
(19,'P109','S104',209,1,'2026-06-02'),
(20,'P110','S105',210,5,'2026-06-02');
insert into sales values
(21,'P103','S101',201,2,'2026-06-03');
select * from sales;
update sales
set quantity=4
where sale_id=21;
delete from sales
where sale_id=21;
delimiter //
create procedure daily_sales_report()
begin
select
store_id,
sale_date,
sum(quantity) as total_sales
from sales
group by store_id,sale_date;
end //
delimiter ;
call daily_sales_report();
show tables;
select * from stores;
select count(*) from stores;
select * from products;
select * from employees;
select count(*) from employees;
select * from sales;
select count(*) from sales;
select
s.sale_id,
p.product_name,
st.store_name,
e.employee_name,
s.quantity
from sales s
join products p
on s.product_id = p.product_id
join stores st
on s.store_id = st.store_id
join employees e
on s.employee_id = e.employee_id;
call daily_sales_report();







