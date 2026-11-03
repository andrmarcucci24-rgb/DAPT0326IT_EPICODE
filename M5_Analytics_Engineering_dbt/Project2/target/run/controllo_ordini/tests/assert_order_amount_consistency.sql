
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  -- Restituisce gli ordini in cui l'importo non corrisponde a quantità x prezzo unitario.
-- Se la query restituisce righe, il test fallisce.
select
    order_id,
    customer_id,
    quantity,
    unit_price,
    amount,
    quantity * unit_price as amount_atteso
from "ecommerce"."main"."raw_orders"
where abs(amount - quantity * unit_price) > 0.01
  
  
      
    ) dbt_internal_test