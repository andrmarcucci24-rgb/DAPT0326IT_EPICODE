{{ config(materialized='table') }}
 
select
   c.city,
   round(sum(o.amount), 2) as fatturato,
   count(*) as numero_ordini
from {{ source('flusso', 'ordini') }} as o
join {{ source('flusso', 'clienti') }} as c
   on o.customer_id = c.customer_id
group by c.city
order by fatturato desc