-- Write your PostgreSQL query statement below
SELECT x, y, z, CASE 
                WHEN x + y > z AND x+z>y AND z+y>x AND x+y+z>0 THEN 'Yes'
                ELSE 'No'
                END as triangle
                FROM Triangle;