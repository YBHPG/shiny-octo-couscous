SELECT sum(total_cost) as sum,
    user_id
FROM reserved_product_payment.order
WHERE month(order_date) < 4
    AND year(order_date) = 2013
GROUP BY user_id