insert `order`(
        user_id,
        order_date,
        ordered_number,
        total_cost,
        status,
        product_code
    )
values(
        '$user_id',
        '$order_date',
        '$ordered_number',
        '$total_cost',
        '1',
        '$product_code'
    )