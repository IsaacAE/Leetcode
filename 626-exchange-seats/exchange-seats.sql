-- Write your PostgreSQL query statement below

SELECT id, 
    (CASE 
        WHEN id % 2 = 0 THEN LAG(student, 1) OVER (
            ORDER BY
            id)
        WHEN id % 2 = 1 AND id <> (SELECT MAX(id) FROM Seat) THEN LEAD(student, 1) OVER (
            ORDER BY
            id)
        ELSE student
        END)
         as student
        
FROM Seat;