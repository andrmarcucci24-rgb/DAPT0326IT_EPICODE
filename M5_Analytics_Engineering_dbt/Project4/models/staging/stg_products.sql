select
    product_id,
    product_name,
    category,
    list_price,
    is_active
from {{ source('ecommerce', 'raw_products') }}
