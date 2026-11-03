
  
    
    
    create  table
      "ecommerce_prod"."main"."stg_orders__dbt_tmp"
  
    as (
      select
    *,
    'prod' as ambiente
from "ecommerce_prod"."main"."raw_orders"
    );
  
    
  