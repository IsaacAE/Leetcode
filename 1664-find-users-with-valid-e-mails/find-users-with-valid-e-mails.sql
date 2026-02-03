-- Write your PostgreSQL query statement below
SELECT *
FROM Users
WHERE REGEXP_INSTR(mail, '^[A-Za-z][A-Za-z0-9_.-]*@leetcode\.com$') > 0;