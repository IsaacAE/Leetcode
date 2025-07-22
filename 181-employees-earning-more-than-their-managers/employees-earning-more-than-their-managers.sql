-- Write your PostgreSQL query statement below
select e.name as Employee from Employee e inner join Employee g on e.managerId = g.id where e.salary > g.salary;