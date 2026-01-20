-- Write your PostgreSQL query stateme
select DISTINCT w1.id
from Weather w1 inner join
     Weather w2
     ON w1.recordDate = w2.recordDate + INTERVAL '1 day'
where w1.temperature > w2.temperature;