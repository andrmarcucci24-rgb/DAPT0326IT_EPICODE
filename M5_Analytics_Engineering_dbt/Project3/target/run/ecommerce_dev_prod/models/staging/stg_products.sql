
  
    
    
    create  table
      "ecommerce_prod"."main"."stg_products__dbt_tmp"
  
    as (
      select * from "ecommerce_prod"."main"."raw_products"
    );
  
    
  