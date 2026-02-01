-- Write your PostgreSQL query statement below
WITH ConsecutiveCheck AS (
    SELECT
        *,
        LAG(num, 1) OVER (ORDER BY id) AS prev_num_1,
        LAG(num, 2) OVER (ORDER BY id) AS prev_num_2
    FROM
        Logs 
)
SELECT DISTINCT
    num as ConsecutiveNums
FROM
    ConsecutiveCheck
WHERE
    num = prev_num_1 AND num = prev_num_2;