select product_id,
    product_category,
    product_name,
    unit_cost
from product
where product_id = '$product_id'