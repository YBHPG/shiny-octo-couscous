select product_id,
    product_category,
    product_name,
    unit_cost
from product
where (quantity > 0)
    and product_id = '$product_id'