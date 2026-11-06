select
    order_item_id,
    order_id,
    product_id,
    quantity,
    line_amount
from {{ source('ecommerce', 'raw_order_items') }}
