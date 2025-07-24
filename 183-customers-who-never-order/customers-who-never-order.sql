-- Write your PostgreSQL query statement below
select e.name as Customers from Customers e where not exists (select * from Orders a where a.customerId = e.id);