-- Write your PostgreSQL query statement below
SELECT max(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT Max(salary) FROM Employee)