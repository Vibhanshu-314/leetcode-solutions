# Write your MySQL query statement below
select e.name
from Employee e
join Employee m
on e.id=m.managerId
GROUP BY e.id, e.name
HAVING COUNT(m.id) >= 5;