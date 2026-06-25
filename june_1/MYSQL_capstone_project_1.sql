create database retail_capstone_db;
use retail_capstone_db; 
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    city VARCHAR(50),
    state VARCHAR(50),
    gender VARCHAR(10),
    membership_type VARCHAR(30)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    order_status VARCHAR(30),
    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
    item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id)
        REFERENCES orders(order_id),
    FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);

CREATE TABLE payments (
    payment_id INT PRIMARY KEY,
    order_id INT,
    payment_mode VARCHAR(30),
    payment_status VARCHAR(30),
    amount DECIMAL(10,2),
    FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
);

CREATE TABLE deliveries (
    delivery_id INT PRIMARY KEY,
    order_id INT,
    delivery_partner VARCHAR(50),
    delivery_status VARCHAR(30),
    delivery_city VARCHAR(50),
    FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
);
insert into customers values
(1,'arun kumar','chennai','tamil nadu','male','gold'),
(2,'priya','madurai','tamil nadu','female','silver'),
(3,'karthik','coimbatore','tamil nadu','male','gold'),
(4,'divya','trichy','tamil nadu','female','platinum'),
(5,'vignesh','chennai','tamil nadu','male','silver'),
(6,'keerthana','salem','tamil nadu','female','gold'),
(7,'suresh','madurai','tamil nadu','male','silver'),
(8,'nandhini','chennai','tamil nadu','female','platinum'),
(9,'prakash','erode','tamil nadu','male','gold'),
(10,'harini','coimbatore','tamil nadu','female','silver');
insert into orders values
(1001,1,'2026-01-05','delivered'),
(1002,2,'2026-01-08','delivered'),
(1003,3,'2026-01-10','pending'),
(1004,4,'2026-01-12','cancelled'),
(1005,5,'2026-01-15','delivered'),
(1006,1,'2026-01-18','delivered'),
(1007,6,'2026-01-20','pending'),
(1008,7,'2026-01-22','delivered'),
(1009,8,'2026-01-24','delivered'),
(1010,9,'2026-01-26','cancelled'),
(1011,10,'2026-01-28','pending'),
(1012,2,'2026-02-01','delivered'),
(1013,3,'2026-02-03','delivered'),
(1014,5,'2026-02-05','pending'),
(1015,8,'2026-02-07','delivered');
insert into products values
(101,'samsung mobile','electronics',18000.00),
(102,'boat earphones','electronics',1500.00),
(103,'laptop','electronics',55000.00),
(104,'smart watch','electronics',3500.00),
(105,'t shirt','fashion',800.00),
(106,'jeans','fashion',1500.00),
(107,'sports shoes','fashion',2500.00),
(108,'office chair','furniture',5000.00),
(109,'study table','furniture',7000.00),
(110,'bluetooth speaker','electronics',3000.00);
insert into order_items values
(1,1001,101,12),
(2,1001,102,25),
(3,1002,105,18),
(4,1002,106,14),
(5,1003,103,22),
(6,1004,107,11),
(7,1005,108,16),
(8,1005,110,13),
(9,1006,104,27),
(10,1006,105,19),
(11,1007,109,15),
(12,1008,102,24),
(13,1009,103,17),
(14,1010,106,21),
(15,1011,101,10),
(16,1012,107,28),
(17,1013,110,23),
(18,1014,108,20),
(19,1015,104,26),
(20,1015,105,29);
insert into payments values
(1,1001,'upi','success',21000.00),
(2,1002,'card','success',3900.00),
(3,1003,'upi','success',55000.00),
(4,1004,'net banking','failed',5000.00),
(5,1005,'card','success',8000.00),
(6,1006,'upi','success',7800.00),
(7,1007,'cash on delivery','pending',7000.00),
(8,1008,'upi','success',3000.00),
(9,1009,'card','success',55000.00),
(10,1010,'upi','failed',3000.00),
(11,1011,'net banking','success',18000.00),
(12,1012,'upi','success',7500.00),
(13,1013,'card','success',6000.00),
(14,1014,'cash on delivery','pending',5000.00),
(15,1015,'upi','success',5100.00);
insert into deliveries values
(1,1001,'delhivery','delivered','chennai'),
(2,1002,'ecom express','delivered','madurai'),
(3,1003,'delhivery','pending','coimbatore'),
(4,1004,'xpressbees','cancelled','trichy'),
(5,1005,'ecom express','delivered','chennai'),
(6,1006,'delhivery','delivered','chennai'),
(7,1007,'xpressbees','pending','salem'),
(8,1008,'delhivery','delivered','madurai'),
(9,1009,'ecom express','delivered','chennai'),
(10,1010,'xpressbees','cancelled','erode'),
(11,1011,'delhivery','pending','coimbatore'),
(12,1012,'ecom express','delivered','madurai'),
(13,1013,'delhivery','delivered','coimbatore'),
(14,1014,'xpressbees','pending','chennai'),
(15,1015,'ecom express','delivered','chennai');
select * from customers;
select customer_name,city,membership_type from customers;
select * from products order by price desc;
update customers
set city = 'hyderabad',
    state = 'telangana'
where customer_id = 2;
update customers
set city = 'hyderabad',
    state = 'telangana'
where customer_id = 4;
select * from customers where city='hyderabad';
select * from customers where membership_type='gold';
select * from products where price between 500 and 5000;
select * from products where category in ('electronics',
'fashion');
select * from orders where order_date> 2026-01-01; 
select  * from payments where payment_mode ='upi';
select * from deliveries where delivery_status='pending';
select count(*) as total  from customers;
select count(*) as total_order from orders;
select count(*) as total_product from products;
select sum(amount) as total_revenue from payments where
payment_status='success';
select avg(amount) as average from payments;
select max(amount) as highest_payment from payments;
select min(amount) as lowest_payment from payments;
select city, count(*) as count from customers group by city;
select category, count(*) as count from products group by 
category;
select order_status , count(*) as total_order 
from orders group by order_status;
select c.customer_name,
o.order_id,
o.order_date from 
customers c left join orders o 
on c.customer_id=o.customer_id;
select oi.order_id,
p.product_name,
oi.quantity,
p.price from order_items oi left join products p 
on oi.product_id = p.product_id;
select c.customer_name, p.product_name, oi.quantity, o.order_date
from customers c
join orders o
on c.customer_id = o.customer_id
join order_items oi
on o.order_id = oi.order_id
join products p
on oi.product_id = p.product_id;
select o.order_id,
p.payment_mode,
p.payment_status,
p.amount from orders o
join payments p
on o.order_id=p.order_id;
select o.order_id, d.delivery_partner, d.delivery_status
from orders o
join deliveries d
on o.order_id = d.order_id;
select c.customer_name,
       c.city,
       o.order_id,
       o.order_date,
       p.product_name,
       p.category,
       oi.quantity,
       p.price,
       pay.payment_status,
       d.delivery_status
from customers c
join orders o
on c.customer_id = o.customer_id
join order_items oi
on o.order_id = oi.order_id
join products p
on oi.product_id = p.product_id
join payments pay
on o.order_id = pay.order_id
join deliveries d
on o.order_id = d.order_id;
select c.city,
       sum(pay.amount) as total_revenue
from customers c
join orders o
on c.customer_id = o.customer_id
join payments pay
on o.order_id = pay.order_id
where pay.payment_status = 'success'
group by c.city;
select c.customer_name,
       sum(pay.amount) as total_revenue
from customers c
join orders o
on c.customer_id = o.customer_id
join payments pay
on o.order_id = pay.order_id
where pay.payment_status = 'success'
group by c.customer_name;
select p.product_name,
       sum(oi.quantity) as total_quantity
from products p
join order_items oi
on p.product_id = oi.product_id
group by p.product_name;
select p.category,
       sum(oi.quantity * p.price) as revenue
from products p
join order_items oi
on p.product_id = oi.product_
select c.customer_name,
       count(o.order_id) as total_orders
from customers c
join orders o
on c.customer_id = o.customer_id
group by c.customer_name;
select c.customer_name,
       count(o.order_id) as total_orders
from customers c
join orders o
on c.customer_id = o.customer_id
group by c.customer_name
having count(o.order_id) > 1;
select p.category,
       sum(oi.quantity * p.price) as revenue
from products p
join order_items oi
on p.product_id = oi.product_id
group by p.category
having sum(oi.quantity * p.price) > 10000;
select city,
       count(*) as total_customers
from customers
group by city
having count(*) > 2;
       sum(oi.quantity) as total_quantity
from products p
join order_items oi
on p.product_id = oi.product_id
group by p.product_name
having sum(oi.quantity) > 3;
select * from customers where customer_id in 
(select customer_id from orders);
insert into customers values
(11,'mohan','vellore','tamil nadu','male','silver');
select * from customers where customer_id not in 
(select customer_id from orders);
insert into products values
(111,'wireless mouse','electronics',1200.00);
select * from products where product_id not in 
(select product_id from order_items );
select *
from payments
where amount >
(
    select avg(amount)
    from payments
);
select c.customer_name
from customers c
join orders o
on c.customer_id = o.customer_id
join payments p
on o.order_id = p.order_id
where p.amount =
(
    select max(amount)
    from payments
);
select distinct c.customer_name
from customers c
join orders o
on c.customer_id = o.customer_id
join order_items oi
on o.order_id = oi.order_id
join products p
on oi.product_id = p.product_id
where p.category ='electronics';
select *
from orders
where order_id in
(
    select order_id
    from payments
    where payment_status = 'success'
);
select *
from orders
where order_id in
(
    select order_id
    from deliveries
    where delivery_status <> 'delivered'
);
select c.customer_name,
       sum(p.amount) as total_spending
from customers c
join orders o
on c.customer_id = o.customer_id
join payments p
on o.order_id = p.order_id
group by c.customer_id, c.customer_name
having sum(p.amount) >
(
    select avg(customer_total)
    from
    (
        select sum(p.amount) as customer_total
        from customers c
        join orders o
        on c.customer_id = o.customer_id
        join payments p
        on o.order_id = p.order_id
        group by c.customer_id
    ) as avg_spending
);
insert into orders values
(1016,1,'2026-02-10','pending');
insert into payments values
(16,1001,'upi','failed',0);
insert into orders values
(1017,2,'2026-02-11','pending');
insert into payments values
(17,1017,'upi','success',2500);
select *
from orders
where order_id not in
(
    select order_id
    from payments
);
select *
from orders
where order_id not in
(
    select order_id
    from deliveries
);
select *
from payments
where amount is null
or amount = 0;
select o.*
from orders o
join payments p
on o.order_id = p.order_id
where o.order_status = 'cancelled'
and p.payment_status = 'success'
select o.*
from orders o
join deliveries d
on o.order_id = d.order_id
join payments p
on o.order_id = p.order_id
where d.delivery_status = 'delivered'
and p.payment_status = 'failed';
select *
from order_items
where product_id not in
(
    select product_id
    from products
);
select *
from orders
where customer_id not in
(
    select customer_id
    from customers
);
