-- Write your PostgreSQL query statement below
SELECT x, y, z, CASE 
                WHEN x < 1 OR z < 1 OR y < 1 THEN 'No'
                WHEN x + y > z AND x + z > y AND z + y > x THEN 'Yes'
                ELSE 'No'
                END as triangle
                FROM Triangle;