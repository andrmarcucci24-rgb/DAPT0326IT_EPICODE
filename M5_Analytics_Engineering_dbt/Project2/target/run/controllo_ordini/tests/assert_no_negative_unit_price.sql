
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  -- Restituisce gli ordini con prezzo unitario negativo.
-- Se la query restituisce righe, il test fallisce.
select
    order_id,
    customer_id,
    quantity,
    unit_price,
    amount
from "ecommerce"."main"."raw_orders"
where unit_price < 0
  
  
      
    ) dbt_internal_test