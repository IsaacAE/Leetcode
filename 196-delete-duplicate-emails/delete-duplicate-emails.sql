-- Write your PostgreSQL query statement below
DELETE FROM Person where id not in (select min(id) from Person group by email having count(email) >= 1);