-- Write your PostgreSQL query statement below
SELECT max(salary) as SecondHighestSalary
from Employee
where salary < (SELECT Max(salary) from Employee)