# Write your MySQL query statement below
select a.id from weather a join weather b on b.temperature < a.temperature where datediff(a.recorddate,b.recorddate) = 1 