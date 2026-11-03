
  
    
    
    create  table
      "ecommerce_prod"."main"."stg_orders_items__dbt_tmp"
  
    as (
      select * from "ecommerce_prod"."main"."raw_order_items"
    );
  
    
  