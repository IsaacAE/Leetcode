-- Write your PostgreSQL query statement below
SELECT id, COUNT(friend) as num
FROM (
    SELECT requester_id as id, accepter_id as friend FROM RequestAccepted
    UNION
    SELECT accepter_id as id, requester_id as friend FROM RequestAccepted
)
GROUP BY id
ORDER BY num DESC
LIMIT 1