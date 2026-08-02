# Write your MySQL query statement below
#SELECT firstName,lastName,city,state From Person 
#LEFT JOIN Address
#on Person.personId =Address.personId;
select p.firstName,p.lastName,a.city,a.state
from Person p
left join Address a
on p.personId=a.personId;