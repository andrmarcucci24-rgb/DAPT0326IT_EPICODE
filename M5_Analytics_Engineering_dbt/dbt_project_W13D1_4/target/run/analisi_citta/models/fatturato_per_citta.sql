
  
    
    
    create  table
      "flusso"."main"."fatturato_per_citta__dbt_tmp"
  
    as (
      
 
select
   c.city,
   round(sum(o.amount), 2) as fatturato,
   count(*) as numero_ordini
from "flusso"."main"."ordini" as o
join "flusso"."main"."clienti" as c
   on o.customer_id = c.customer_id
group by c.city
order by fatturato desc
    );
  
    
  