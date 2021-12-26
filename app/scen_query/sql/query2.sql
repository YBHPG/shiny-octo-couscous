SELECT product_id,
    product_category,
    product_name,
    material,
    measurement_units,
    unit_cost,
    quantity,
    reserved_count
FROM product
where product_id = '$product_id'