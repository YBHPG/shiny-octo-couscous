SELECT user_id,
    sum(total_cost) as sum
FROM reserved_product_payment.order
WHERE month(order_date) = '$month'
    AND year(order_date) = '$year'
    AND user_id = '$user_id'
GROUP BY user_id