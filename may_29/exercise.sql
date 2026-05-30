-- use retail_db;
/*select * from products where product_name like '%k';
select * from products where product_name like '%top%';*/

/*select product_name as product,
price as productprice from products;*/
-- select * from products order by price desc ;
 -- select COUNT(*) from products;
 /*select count(*) from products where category='electronics';
 select sum(price) from products;*/
 
 /*select 
 count(*) as totalproducts,
 sum(price) as totalprice,
 avg(price) as averageprice,
 max(price) as highestprice,
 min(price) as lowestprice from products;
 */
 select category,sum(price) as totalprice from products group by category;
