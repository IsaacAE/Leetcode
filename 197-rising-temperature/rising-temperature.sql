-- Write your PostgreSQL query stateme
select DISTINCT w2.id
from Weather w2 inner join
     Weather w1
     ON w2.recordDate = w1.recordDate + INTERVAL '1 day'
where w1.temperature < w2.temperature;