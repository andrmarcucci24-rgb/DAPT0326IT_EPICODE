-- created_at: 2026-11-03T19:32:29.261137800+00:00
-- finished_at: 2026-11-03T19:32:29.264001200+00:00
-- elapsed: 2ms
-- outcome: success
-- dialect: duckdb
-- node_id: test.controllo_ordini.assert_order_amount_consistency
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "dbt_version": "2.0.0", "node_id": "test.controllo_ordini.assert_order_amount_consistency", "profile_name": "controllo_ordini", "target_name": "dev"} */

    
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
  
  
      
    ) dbt_internal_test;

-- created_at: 2026-11-03T19:32:29.261137800+00:00
-- finished_at: 2026-11-03T19:32:29.264000500+00:00
-- elapsed: 2ms
-- outcome: success
-- dialect: duckdb
-- node_id: test.controllo_ordini.assert_no_negative_unit_price
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "dbt_version": "2.0.0", "node_id": "test.controllo_ordini.assert_no_negative_unit_price", "profile_name": "controllo_ordini", "target_name": "dev"} */

    
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
  
  
      
    ) dbt_internal_test;

