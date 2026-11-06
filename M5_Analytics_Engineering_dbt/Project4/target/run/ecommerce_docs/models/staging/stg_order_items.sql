
  
  create view "ecommerce"."main"."stg_order_items__dbt_tmp" as (
    select
    order_item_id,
    order_id,
    product_id,
    quantity,
    line_amount
from "ecommerce"."main"."raw_order_items"
  );
