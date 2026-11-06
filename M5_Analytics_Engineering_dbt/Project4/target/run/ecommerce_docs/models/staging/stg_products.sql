
  
  create view "ecommerce"."main"."stg_products__dbt_tmp" as (
    select
    product_id,
    product_name,
    category,
    list_price,
    is_active
from "ecommerce"."main"."raw_products"
  );
