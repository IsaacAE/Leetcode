-- Write your PostgreSQL query statement below
SELECT Department.name as Department, Employee.name as Employee, Employee.salary as Salary FROM Department JOIN (SELECT 
        *,
        RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) as ranking
    FROM Employee) as Employee ON Department.id= Employee.departmentId WHERE ranking = 1;