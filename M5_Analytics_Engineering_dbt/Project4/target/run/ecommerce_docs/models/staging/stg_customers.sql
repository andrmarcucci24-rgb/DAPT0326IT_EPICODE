
  
  create view "ecommerce"."main"."stg_customers__dbt_tmp" as (
    select
    customer_id,
    customer_name,
    city,
    customer_segment,
    signup_date
from "ecommerce"."main"."raw_customers"
  );
