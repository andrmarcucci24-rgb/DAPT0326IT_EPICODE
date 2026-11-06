
  
  create view "ecommerce"."main"."stg_orders__dbt_tmp" as (
    select
    cast(order_id as bigint) as order_id,
    cast(customer_id as bigint) as customer_id,
    order_date,
    status,
    quantity,
    unit_price,
    amount
from "ecommerce"."main"."raw_orders"
  );
