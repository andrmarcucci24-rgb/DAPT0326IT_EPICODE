select
    customer_id,
    customer_name,
    city,
    customer_segment,
    signup_date
from {{ source('ecommerce', 'raw_customers') }}
