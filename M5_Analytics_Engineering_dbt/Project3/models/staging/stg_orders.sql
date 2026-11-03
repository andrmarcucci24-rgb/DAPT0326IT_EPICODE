select
    *,
    '{{ target.name }}' as ambiente
from {{ source('ecommerce', 'raw_orders') }}
