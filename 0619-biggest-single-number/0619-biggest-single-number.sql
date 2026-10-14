
select MAX(num) as num
from MyNumbers
where num not in(select num 
            from MyNumbers 
            group by num 
            having count(*)>1);