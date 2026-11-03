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