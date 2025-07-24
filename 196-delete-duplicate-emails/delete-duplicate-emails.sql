# Write your MySQL query statement below
DELETE c1
FROM Person c1
JOIN Person c2
ON c1.email = c2.email AND c1.id > c2.id;