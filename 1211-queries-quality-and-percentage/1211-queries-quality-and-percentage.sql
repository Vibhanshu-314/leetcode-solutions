# Write your MySQL query statement below
select
    query_name,
    round(sum(rating/position)/count(*),2) as quality , 
    round(sum(case when rating<3 then 1 else 0 end)*100.0/count(*),2) as poor_query_percentage

from
   Queries
where
   query_name is not null
group by
   query_name;       





#SELECT 
#    query_name,
#    ROUND(AVG(rating / position), 2) AS quality,
#    ROUND(SUM(rating < 3) * 100.0 / COUNT(*), 2) AS #poor_query_percentage
#FROM 
#    Queries
#WHERE 
#    query_name IS NOT NULL
#GROUP BY 
#    query_name;   